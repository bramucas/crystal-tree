"""
This file implements the class ScikitLearnAdapter. the adapter for the scikit-learn library.
"""
import numpy as np
from ._base_tree_adapter import BaseTreeAdapter


class ScikitLearnAdapter(BaseTreeAdapter):
    """ Translates a scikit-learn DecisionTreeClassifier to a logic program.

    Args:
        dt (DecisionTreeClassifier or RandomForestClassifier): the scikit-learn model to be adapted.
        feature_names (list, optional): the names of the features. Defaults to None.
        factor (int, optional): the factor to be used to round the thresholds. Defaults to 0.
    """
    def __init__(self, dt):
        self.n_nodes = dt.tree_.node_count
        self.children_left = dt.tree_.children_left
        self.children_right = dt.tree_.children_right
        self.feature = dt.tree_.feature
        self.threshold = dt.tree_.threshold
        self.value = dt.tree_.value


    def _thresholds(self, factor):
        mult = 10**factor
        return "\n".join([f'thres({int(v*mult)}).' for v in set(self.threshold) if v>0])

    def which_class(self, val):
        """_summary_

        Args:
            val (_type_): _description_

        Returns:
            _type_: _description_
        """
        max_index = list(val[0]).index(max(val[0]))
        proba = int(max(val[0]) / sum(val[0]) * 100)
        return f'class({max_index},I, {proba})'

    def __write_rule(self, factor, stack):
        mult = 10**factor
        nid, _ = stack.pop()
        head = self.which_class(self.value[nid])

        literals = []
        min_max = {
            feature: {"min_gt": -np.inf, "max_le": np.inf} for feature in range(max(self.feature)+1)
        }
        while stack:
            nid, right = stack.pop()
            feature, thres = self.feature[nid], self.threshold[nid]

            if right and thres>min_max[feature]["min_gt"]:
                min_max[feature]["min_gt"]=thres
            if not right and thres<min_max[feature]["max_le"]:
                min_max[feature]["max_le"]=thres

        for feature, values in min_max.items():
            fval = f'{feature}'
            if not np.isinf(values["min_gt"]) and not np.isinf(values["max_le"]):
                literals.append(f'between(I,{fval},{int(values["min_gt"]*mult)},{int(values["max_le"]*mult)})')
            elif np.isinf(values["min_gt"]) and not np.isinf(values["max_le"]):
                literals.append(f'le(I,{fval},{int(values["max_le"]*mult)})')
            elif np.isinf(values["max_le"]) and not np.isinf(values["min_gt"]):
                literals.append(f'gt(I,{fval},{int(min_max[feature]["min_gt"]*mult)})')

        rule = f'{head} :- {", ".join(literals)}.'
        return rule

    def _stacked_rule_per_leaf(self, factor, stack=None):
        if stack is None:
            return f'{self._stacked_rule_per_leaf(factor, [(0, False)])}\n{self._stacked_rule_per_leaf(factor, [(0, True)])}'
    
        parent_id, was_right = stack[-1]
        nid = self.children_right[parent_id] if was_right else self.children_left[parent_id]
        left, right = self.children_left[nid], self.children_right[nid]
        if left == right:  ## nid is leaf
            return self.__write_rule(factor, stack + [(nid, -1)])
        else:
            return f'{self._stacked_rule_per_leaf(factor, stack +  [(nid, False)])}\n{self._stacked_rule_per_leaf(factor, stack +  [(nid, True)])}'

    def _rule_per_leaf(self, factor):
        return self._stacked_rule_per_leaf(factor, stack=None)
