from sklearn.tree import DecisionTreeClassifier
from sklearn.tree._tree import Tree

import numpy as np

_DEFAULT_TRACES= \
"""%!trace {"Good forecast (>5 years)", P} alive(P).
%!trace {"Bad forecast (<5years)", P} not_alive(P).

%!trace {"% is true",F} holds(P,F,true).
%!trace {"% is false",F} holds(P,F,false). 

%!trace {"% > %", F, T} gt(P,F,T).
%!trace {"% <= %", F, T} le(P,F,T).
%!trace {"% in (%,%]", F, Min, Max} between(P,F,Min,Max)."""

_DEFAULT_EXTRA_LOCATION="default_extra.lp"

class CrystalTree():
       
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
        
        self.feature_names = feature_names
        
    @property
    def traces(self):
        if not hasattr(self, '_traces'):
            with open(_DEFAULT_TRACES_LOCATION, 'r') as traces_files:
                setattr(self, '_traces', traces_files.read())
        return self._traces

    @property
    def extra(self):
        if not hasattr(self, '_extra'):
            with open(_DEFAULT_TRACES_LOCATION, 'r') as extra_files:
                setattr(self, '_extra', extra_files.read())
        return self._extra

        
    def _thresholds(self):
        return "\n".join([f'thres({int(v*100)}).' for v in set(self.threshold) if v>0]) 

    def which_class(self, val):
        if val[0][0] >= val[0][1]:
            return "alive(P)"
        else:
            return "not_alive(P)"

    def __write_rule(self, stack):
        nid, _ = stack.pop()
        head = self.which_class(self.value[nid])

        literals = []
        min_max = {
            "rec_afp": {"min_gt": -np.inf, "max_le": np.inf},
            "don_microesteatosis": {"min_gt": -np.inf, "max_le": np.inf},
            "rec_provenance": {"min_gt": -np.inf, "max_le": np.inf},
        }
        while stack:
            nid, right = stack.pop()
            f, t = self.feature_names[self.feature[nid]], self.threshold[nid]
            if f in min_max:
                if right and t>min_max[f]["min_gt"]:
                    min_max[f]["min_gt"]=t
                if not right and t<min_max[f]["max_le"]:
                    min_max[f]["max_le"]=t
            else:
                literals.append(f'holds(P,{f},{"true" if right else "false"})')

        for f, vs in min_max.items():
            if not np.isinf(vs["min_gt"]) and not np.isinf(vs["max_le"]):
                literals.append(f'between(P,{f},{int(vs["min_gt"]*100)},{int(vs["max_le"]*100)})')
            elif np.isinf(vs["min_gt"]) and not np.isinf(vs["max_le"]):
                literals.append(f'le(P,{f},{int(vs["max_le"]*100)})')
            elif np.isinf(vs["max_le"]) and not np.isinf(vs["min_gt"]):
                literals.append(f'gt(P,{f},{int(min_max[f]["min_gt"]*100)})')

        rule = f'{head} :- {", ".join(literals)}.'
#         print(rule)
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
            
    def to_paths(self, include_traces=True):
        return "%%% thresholds\n{thresholds}%%% paths\n{program}\n\n".format(
            program=self._rule_per_leaf(),
            thresholds=self._thresholds(),
        )

    def rule_per_node_escalonado(self, include_traces=True):
        node = lambda node, side: f'tree_node({node},P,{side})'
        write_holds = lambda f, v: f'holds(P,{f},{v})'
        gt = lambda f, v: f'gt(P,{f},{int(v*100)})'
        le = lambda f, v: f'le(P,{f},{int(v*100)})'

        write_bool_trace = lambda f, v: f'{f} is {v}'
        write_gt_trace = lambda f, v: f'{f} > {v}'
        write_le_trace = lambda f, v: f'{f} <= {v}'
        trace = lambda s: f'%!trace_rule {{"{s}"}}'

        def visit_nodes(stack):
            if not stack:
                nid = 0            
            else:
                parent, side = stack[-1]
                nid = self.children_left[parent] if side == "left" else self.children_right[parent]

            f = self.feature_names[self.feature[nid]] if self.feature_names else 2
            t = self.threshold[nid]
            if self.children_left[nid] == self.children_right[nid]:
                return f'{self.which_class(self.value[nid])} :- {node(parent, side)}.\n'
            else:
                parent_condition = "" if nid == 0 else ", "+node(parent, side)
                if f in ("rec_afp", "don_microesteatosis", "rec_provenance"):
                    left_trace_rule = trace(write_le_trace(f, t))
                    node_left_condition  = le(f, t)
                    right_trace_rule = trace(write_gt_trace(f, t))
                    node_right_condition = gt(f, t) 
                else:
                    left_trace_rule = trace(write_bool_trace(f, "false"))
                    node_left_condition  = write_holds(f, "false")
                    right_trace_rule = trace(write_bool_trace(f, "true"))
                    node_right_condition = write_holds(f, "true")

                # %!trace_rule {"{nombre variable} is true/false"}
                # %!trace_rule {"{nombre variable} <=/> num"}

                return "{trace_rule}\n{head} :- {condition}{parent}.\n\n".format(
                    trace_rule=left_trace_rule if include_traces else "",
                    head=node(nid, "left"),
                    condition=node_left_condition,
                    parent=parent_condition
                ) + \
                visit_nodes(stack + [(nid, "left")]) + \
                "{trace_rule}\n{head} :- {condition}{parent}.\n\n".format(
                    trace_rule=right_trace_rule if include_traces else "",
                    head=node(nid, "right"),
                    condition=node_right_condition,
                    parent=parent_condition
                ) + \
                visit_nodes(stack + [(nid, "right")])

        return visit_nodes([])
    
    def write_in_files(self, paths="paths.lp", extra="extra.lp", traces="traces.lp"):
        if extra is not None:
            with open(extra, 'w') as extra_file:
                extra_file.write(self.extra)
        if traces is not None:
            with open(traces, 'w') as traces_file:
                traces_file.write(self.traces)
        if paths is not None:
            with open(paths, 'w') as paths_file:
                paths_file.write(self.to_paths())