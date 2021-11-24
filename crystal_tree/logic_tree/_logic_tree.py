from sklearn.tree import DecisionTreeClassifier
from sklearn.tree._tree import Tree

import numpy as np

from . import defaults_lp

_DEFAULT_EXTRA_LOCATION  = "default_extra.lp"
_DEFAULT_TRACES_LOCATION = "default_traces.lp"

class LogicTree:
    def __init__(self, dt, feature_names=None):
        if isinstance(dt, DecisionTreeClassifier):
            self._tree = dt.tree_
        elif isinstance(dt, Tree):
            self._tree = dt
        else:
            raise NotImplementedError("crystal-tree only supports sklearn decision trees by now.")
            
        self.n_nodes = self._tree.node_count
        self.children_left = self._tree.children_left
        self.children_right = self._tree.children_right
        self.feature = self._tree.feature
        self.threshold = self._tree.threshold
        self.value = self._tree.value

        if feature_names is None:
            self.feature_names = [f'f{i}' for i in range(max(self.feature))]
        else:
            if len(feature_names) != max(self.feature)+1:
                raise ValueError("Feature names length does not match tree data.")
            self.feature_names = feature_names

        self.feature_names = feature_names

    @property
    def traces(self):
        if not hasattr(self, '_traces'):
            try:
                import importlib.resources as pkg_resources
            except ImportError:
                # Try backported to PY<37 `importlib_resources`.
                import importlib_resources as pkg_resources
            setattr(self, '_traces', pkg_resources.read_text(defaults_lp, _DEFAULT_TRACES_LOCATION))
        return self._traces

    @property
    def extra(self):
        if not hasattr(self, '_extra'):
            try:
                import importlib.resources as pkg_resources
            except ImportError:
                # Try backported to PY<37 `importlib_resources`.
                import importlib_resources as pkg_resources
            setattr(self, '_extra', pkg_resources.read_text(defaults_lp, _DEFAULT_EXTRA_LOCATION))
        return self._extra
    
    def _thresholds(self):
        return "\n".join([f'thres({int(v*100)}).' for v in set(self.threshold) if v>0])

    def which_class(self, val):
        max_index = list(val[0]).index(max(val[0]))
        return f'class({max_index},P)'

    def __write_rule(self, stack):
        nid, _ = stack.pop()
        head = self.which_class(self.value[nid])

        literals = []
        min_max = {
            f: {"min_gt": -np.inf, "max_le": np.inf} for f in self.feature_names
        }
        while stack:
            nid, right = stack.pop()
            f, t = self.feature_names[self.feature[nid]], self.threshold[nid]

            if right and t>min_max[f]["min_gt"]:
                min_max[f]["min_gt"]=t
            if not right and t<min_max[f]["max_le"]:
                min_max[f]["max_le"]=t

        for f, vs in min_max.items():
            if not np.isinf(vs["min_gt"]) and not np.isinf(vs["max_le"]):
                literals.append(f'between(P,{f},{int(vs["min_gt"]*100)},{int(vs["max_le"]*100)})')
            elif np.isinf(vs["min_gt"]) and not np.isinf(vs["max_le"]):
                literals.append(f'le(P,{f},{int(vs["max_le"]*100)})')
            elif np.isinf(vs["max_le"]) and not np.isinf(vs["min_gt"]):
                literals.append(f'gt(P,{f},{int(min_max[f]["min_gt"]*100)})')

        rule = f'{head} :- {", ".join(literals)}.'
        return rule

    def _rule_per_leaf(self, stack=None):
        if stack == None:
            return f'{self._rule_per_leaf([(0, False)])}\n{self._rule_per_leaf([(0, True)])}'
        else:
            parent_id, was_right = stack[-1]
            nid = self.children_right[parent_id] if was_right else self.children_left[parent_id]
            left, right = self.children_left[nid], self.children_right[nid]
            if left == right:  ## nid is leaf
                return self.__write_rule(stack + [(nid, -1)])
            else:
                return f'{self._rule_per_leaf(stack +  [(nid, False)])}\n{self._rule_per_leaf(stack +  [(nid, True)])}'
            
    def get_paths(self):
        if not hasattr(self, '_paths'):
            setattr(self, '_paths', 
                "%%% thresholds\n{thresholds}\n%%% paths\n{program}\n\n".format(
                    program=self._rule_per_leaf(),
                    thresholds=self._thresholds(),
                )
            )
        return self._paths