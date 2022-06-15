"""crystal-tree package main classes.
"""
from numpy import asarray

from clingo.symbol import String, SymbolType
from dafact import Dafacter
from xclingo import XclingoControl, XclingoContext

from crystal_tree.logic_tree import LogicTree

class Condition:
    """Encapsules a condition in a logic tree.
    """
    def __init__(self, operator:str, value:str):
        """
        Args:
            operator (str): string representation of the operator. Accepted values: '<', '>', '=', '!=', '<=' or '>='.
            value (str): string representation of the value.
        """
        self.operator = operator
        self.value = value

    def to_atom(self):
        """Returns the condition as a clingo atom.

        Returns:
            str: the atom representation of the condition.
        """        
        return f'V{self.operator}{self.value}'

class Trace:
    """Represents a trace for the logic tree.
    """
    def __init__(self, text, feature, conditions=None, target_class=None):
        """
        Args:
            text (str): text for the text label.
            feature (str): feature which will be affected by the trace.
            conditions (Condition, optional): conditions for the trace to apply. Defaults to None.
            target_class (str, optional): class which will be affected by the trace. Defaults to None.
        """
        self.text = text
        self.feature = feature

        self.conditions = [] if conditions is None else conditions
        self.target_class = target_class
    
    def to_xclingo_code(self):
        """_summary_

        Returns:
            str:         
        """        
        def find_all(s, to_find):
            i = -1
            while True:
                i = s.find(to_find, i+1)
                if i == -1:
                    break
                yield i, to_find

        # check if is prediction or feature
        text = self.text
        variables = []
        if self.feature == "prediction":
            # find if %_class and %_instance and its order
            occurrences = sorted(list(find_all(self.text, "%_class")) + list(find_all(self.text, "%_instance")))
            variables = []
            for _, threshold in occurrences:
                if threshold == "%_class":
                    variables.append("C")
                elif threshold == "%_instance":
                    variables.append("I")
            # change thresholds
            text = self.text.replace("%_class", "%").replace("%_instance", "%")
        
        # builds %!trace theory atom
        xclingo_trace = f'%!trace {{"{text}",{",".join([v for v in variables])}}}'
        
        # builds conditional atom
        conditional_atom = 'prediction(I) : ' if self.feature == "prediction" else  f'holds(I,{self.feature},V) : '
        
        conditions = []
        conditions += [c.to_atom() for c in self.conditions]
        if self.target_class is not None:
            conditions.append('class(C,I)')
            conditions.append(f'C={self.target_class}')

        xclingo_trace += ' ' + conditional_atom + ','.join(conditions) + '.'
        return xclingo_trace

class CrystalTreeContext(XclingoContext):
    """_summary_

    Args:
        XclingoContext (_type_): _description_
    """
    def __init__(self, factor=0):
        super().__init__()
        self.div = 10**factor

    @staticmethod
    def next_is_threshold(string):
        """_summary_

        Args:
            string (_type_): _description_

        Returns:
            _type_: _description_
        """
        idx = string.index("%")
        return string[idx:idx+3] == "%_t"

    def label(self, text, tup):
        """_summary_

        Args:
            text (_type_): _description_
            tup (_type_): _description_

        Returns:
            _type_: _description_
        """
        if text.type == SymbolType.String:
            text = text.string
        else:
            text = str(text).strip('"')
        for val in tup.arguments:
            if self.next_is_threshold(text):
                text = text.replace("%_t", str(val.number/self.div), 1)
            else:
                val_str = val.string if val.type==SymbolType.String else str(val)
                text = text.replace("%", val_str, 1)
        return [String(text)]

class CrystalTree():
    """_summary_
    """
    def __init__(self, dt, feature_names=None, factor=None):
        self._dt = dt
        self.predict = self._dt.predict

        self.feature_names = feature_names
        self.factor = factor
        self.prediction_traces = []
        self.feature_traces = []

        self._logic_tree = None
    
    def to_annotated_logic_program(self, paths="paths.lp", extra="extra.lp", traces="traces.lp", feature_names=None, factor=None):
        """_summary_

        Args:
            paths (str, optional): _description_. Defaults to "paths.lp".
            extra (str, optional): _description_. Defaults to "extra.lp".
            traces (str, optional): _description_. Defaults to "traces.lp".
            feature_names (_type_, optional): _description_. Defaults to None.
            factor (_type_, optional): _description_. Defaults to None.

        Raises:
            RuntimeError: _description_
        """
        if self._logic_tree is None:
            if factor is None:
                raise RuntimeError('argument factor can not be None')
            self._logic_tree = LogicTree(self._dt, feature_names=feature_names, factor=factor)
        if extra is not None:
            with open(extra, 'w') as extra_file:
                extra_file.write(self._logic_tree.extra)
        if traces is not None:
            with open(traces, 'w') as traces_file:
                traces_file.write(self._logic_tree.prediction_traces)
                traces_file.write(self._logic_tree.feature_traces)
        if paths is not None:
            with open(paths, 'w') as paths_file:
                paths_file.write(self._logic_tree.get_paths())

    def set_logic_tree(self, feature_names=None, factor=None):
        """_summary_

        Args:
            feature_names (_type_, optional): _description_. Defaults to None.
            factor (_type_, optional): _description_. Defaults to None.

        Raises:
            RuntimeError: _description_
        """
        if factor is None:
            raise RuntimeError('argument factor can not be None')
        self._logic_tree = LogicTree(self._dt, feature_names=feature_names, factor=factor)

    def max_decimal_places(self, matrix_2d):
        """_summary_

        Args:
            matrix_2d (_type_): _description_
        """
        def get_decimal_places(number):
            number = str(number).strip('0')
            try:
                return len(number) - number.index('.') - 1
            except ValueError:
                return 0

        matrix_2d = asarray(matrix_2d)
        max = 0
        for col in matrix_2d:
            for val in col:
                places = get_decimal_places(val)
                if places > max:
                    max = places
        return max

    def add_trace(self, trace:Trace):
        """_summary_

        Args:
            trace (Trace): _description_
        """
        if trace.feature == "prediction":
            self.prediction_traces.append(trace)
        else:
            self.feature_traces.append(trace)

    def get_custom_prediction_traces(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return "\n".join([t.to_xclingo_code() for t in self.prediction_traces])

    def get_custom_feature_traces(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return "\n".join([t.to_xclingo_code() for t in self.prediction_traces])

    def explain(self, instances):
        """_summary_

        Args:
            instances (_type_): _description_
        """
        if self.factor is None:
            factor = self.max_decimal_places(instances)
        else:
            factor = self.factor

        if self.feature_names is None and hasattr(instances, 'columns'):
            feature_names = instances.columns
        else:
            feature_names = self.feature_names

        self.set_logic_tree(feature_names=feature_names, factor=factor)
        dafacter = Dafacter(instances, feature_names, factor=factor)
        control = XclingoControl(n_solutions=1, n_explanations=0)
        control.add("base", [], dafacter.as_program_string())
        control.add("base", [], self._logic_tree.get_paths())
        control.add("base", [], self._logic_tree.extra)
        if self.prediction_traces:
            control.add("base", [], self.get_custom_prediction_traces())
        else:
            control.add("base", [], self._logic_tree.prediction_traces)
        if self.feature_traces:
            control.add("base", [], self.get_custom_feature_traces())
        else:
            control.add("base", [], self._logic_tree.feature_traces)

        control.ground([("base", [])], explainer_context=CrystalTreeContext(factor))

        return  asarray(list(next(control.explain())))  # should always have only one answer
