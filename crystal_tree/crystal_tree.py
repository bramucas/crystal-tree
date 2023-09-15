"""crystal-tree package main classes.
"""
from numpy import asarray

from clingo.symbol import String, SymbolType
from dafact import Dafacter
from xclingo import XclingoControl, XclingoContext
from crystal_tree.adapters import ScikitLearnAdapter


class Condition:
    """Encapsules a condition in a logic tree.
    
    Parameters
    ----------
        operator: str
            string representation of the operator. Accepted values: '<', '>', '=', '!=', '<=' or '>='.
        value: str
            string representation of the value.
    """
    def __init__(self, operator:str, value:str):
        self.operator = operator
        self.value = value

    def to_atom(self):
        """Returns the condition as a clingo atom.

        Returnns
        --------
            str: the atom representation of the condition.
        """
        return f'V{self.operator}{self.value}'

class Trace:
    """Represents a trace for the logic tree.

    Parameters
    ----------
        text: str
            text for the text label.
        feature: str
            feature which will be affected by the trace.
        conditions: :ref:`list[crystal_tree.Condition]`
            optionalconditions for the trace to apply. Defaults to None.
        target_class: str, optional
            class which will be affected by the trace. Defaults to None.
    """
    def __init__(self, text, feature, conditions=None, target_class=None):
        self.text = text
        self.feature = feature

        self.conditions = [] if conditions is None else conditions
        self.target_class = target_class
    
    def to_xclingo_code(self):
        """Translates the trace object to xclingo code.

        Returns
        -------
            str: string containing the xclingo code translation.
        """
        def _find_all(text, to_find):
            i = -1
            while True:
                i = text.find(to_find, i+1)
                if i == -1:
                    break
                yield i, to_find

        # Checks if is prediction or feature
        text = self.text
        variables = []
        if self.feature == "prediction":
            # Finds if %_class and %_instance and its order
            occurrences = sorted(list(_find_all(self.text, "%_class")) + list(_find_all(self.text, "%_instance")))
            variables = []
            for _, threshold in occurrences:
                if threshold == "%_class":
                    variables.append("C")
                elif threshold == "%_instance":
                    variables.append("I")
            # Changes thresholds
            text = self.text.replace("%_class", "%").replace("%_instance", "%")

        # Builds %!trace theory atom
        xclingo_trace = f'%!trace {{"{text}",{",".join([v for v in variables])}}}'

        # Builds conditional atom
        conditional_atom = 'prediction(I) : ' if self.feature == "prediction" else  f'holds(I,{self.feature},V) : '

        conditions = []
        conditions += [c.to_atom() for c in self.conditions]
        if self.target_class is not None:
            conditions.append('class(C,I,P)')
            conditions.append(f'C={self.target_class}')

        xclingo_trace += ' ' + conditional_atom + ','.join(conditions) + '.'
        return xclingo_trace

class CrystalTreeContext(XclingoContext):
    """Context class needed for correctly generating the explanations through xclingo. It overrides
    the label context function to correclty handle the thresholds.

    Parameters
    ----------
        factor: int, optional
            Factor to be used to round the thresholds. Defaults to zero.
    """
    def __init__(self, factor=0):
        super().__init__()
        self.div = 10**factor

    @staticmethod
    def _next_is_threshold(string):
        idx = string.index("%")
        return string[idx:idx+3] == "%_t"

    def label(self, text, tup):
        """Processes the traces text and handles the thresholds. Overrides the default xclingo's 
        label function.

        Parameters
        ----------
            text: clingo.ast.Atom
                Atom containing label's text.
            tup: clingo.ast.Tuple
                Tuple containing placeholders replacements.
        
        Returns
        -------
            list[clingo.String]: (a list with only one item) the processed label.
        """
        if text.type == SymbolType.String:
            text = text.string
        else:
            text = str(text).strip('"')
        for val in tup.arguments:
            if self._next_is_threshold(text):
                text = text.replace("%_t", str(val.number/self.div), 1)
            else:
                val_str = val.string if val.type==SymbolType.String else str(val)
                text = text.replace("%", val_str, 1)
        return [String(text)]

class CrystalTree:
    """Obtains clear explanations for arbitrarily complex decision trees.

    Parameters
    ----------
    decision_tree : object
        The original decision tree. It can be a scikit-learn DecisionTreeClassifier or from other
        supported packages.
    tree_adapter : :ref:`BaseTreeAdapter`, optional.
        Adapter for the decision tree. Defaults to :ref:`ScikitLearnAdapter`. Other can be found
        in :ref:`crystal_tree.adapters`.
    feature_names : list[str], optional
        Names of the features. Defaults to None.
    factor : int, optional
        Factor to be used to round the thresholds. If None (default), it will be adjusted to
        capture all the decimals within the data at explanation time.
    """
    def __init__(self, decision_tree, tree_adapter=ScikitLearnAdapter):
        self._dt = decision_tree
        self.predict = self._dt.predict

        self.prediction_traces = []
        self.feature_traces = []

        self._logic_tree = tree_adapter(self._dt)

    def _max_decimal_places(self, instances_matrix):
        """Finds the maximum factor needed to capture all decimals within 'instances_matrix'.

        Args:
            matrix_2d (2D array): values for the instances.
        """
        def get_decimal_places(number):
            number = str(number).strip('0')
            try:
                return len(number) - number.index('.') - 1
            except ValueError:
                return 0

        instances_matrix = asarray(instances_matrix)
        max_value = 0
        for col in instances_matrix:
            for val in col:
                places = get_decimal_places(val)
                if places > max_value:
                    max_value = places
        return max_value

    def add_trace(self, trace:Trace):
        """Adds a new trace to the CrystalTree.
        """
        if trace.feature == "prediction":
            self.prediction_traces.append(trace)
        else:
            self.feature_traces.append(trace)

    def _get_custom_prediction_traces(self):
        return "\n".join([t.to_xclingo_code() for t in self.prediction_traces])

    def _get_custom_feature_traces(self):
        return "\n".join([t.to_xclingo_code() for t in self.prediction_traces])

    def explain(self, instances, factor=None, feature_names=None):
        """Obtains the explanation for the given instances.

        Args:
            instances (2Darray): values for the instances.

        Returns:
            NDArray[Any]: explanations for the given instances.
        """

        factor = self._max_decimal_places(instances) if factor is None else factor
        dafacter = Dafacter(instances, factor=factor)
        control = XclingoControl(n_solutions=1, n_explanations=0)
        control.add("base", [], dafacter.as_program_string())
        print(dafacter.as_program_string())
        control.add("base", [], self._logic_tree.get_logic_program(
            factor,
            prediction_traces = None if self.prediction_traces is None
                else self._get_custom_prediction_traces(),
            feature_traces = None if self.feature_traces is None
                else self._get_custom_feature_traces(),
            feature_names = feature_names,
        ))

        control.ground([("base", [])], explainer_context=CrystalTreeContext(factor))

        return  asarray(list(next(control.explain())))  # should always have only one answer
