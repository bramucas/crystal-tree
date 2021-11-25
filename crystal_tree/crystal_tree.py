import dafact
from numpy import asarray
from crystal_tree.logic_tree import LogicTree
from clingo.symbol import String, SymbolType
from dafact import Dafacter
from xclingo import XclingoControl, XclingoContext
from decimal import Decimal

class CrystalTreeContext(XclingoContext):
    def __init__(self, factor=0):
        super().__init__()
        self.div = 10**factor

    @staticmethod
    def next_is_threshold(string):
        idx = string.index("%")
        return string[idx:idx+3] == "%_t"

    def label(self, text, tup):
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
    def __init__(self, dt, feature_names=None, factor=None):
        self._dt = dt
        self.predict = self._dt.predict

        self.feature_names = feature_names
        self.factor = factor

        self._logic_tree = None
    
    def to_annotated_logic_program(self, paths="paths.lp", extra="extra.lp", traces="traces.lp", feature_names=None, factor=None):
        if self._logic_tree is None:
            if factor is None:
                raise RuntimeError('argument factor can not be None')
            self._logic_tree = LogicTree(self._dt, feature_names=feature_names, factor=factor)
        if extra is not None:
            with open(extra, 'w') as extra_file:
                extra_file.write(self._logic_tree.extra)
        if traces is not None:
            with open(traces, 'w') as traces_file:
                traces_file.write(self._logic_tree.traces)
        if paths is not None:
            with open(paths, 'w') as paths_file:
                paths_file.write(self._logic_tree.get_paths())

    def set_logic_tree(self, feature_names=None, factor=None):
        if factor is None:
            raise RuntimeError('argument factor can not be None')
        self._logic_tree = LogicTree(self._dt, feature_names=feature_names, factor=factor)

    def max_decimal_places(self, matrix_2d):
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

    def explain(self, instances):
        if self.factor is None:
            factor = self.max_decimal_places(instances)
        else:
            factor = self.factor
        self.set_logic_tree(feature_names=self.feature_names, factor=factor)
        
        dafacter = Dafacter(instances, self._logic_tree.feature_names, factor=factor)
        control = XclingoControl(n_solutions=1, n_explanations=0)
        control.add("cases", [], dafacter.as_program_string())
        control.add("paths", [], self._logic_tree.get_paths())
        control.add("extra", [], self._logic_tree.extra)
        control.add("traces", [], self._logic_tree.traces)

        control.ground([("base", [])], explainer_context=CrystalTreeContext(factor))
        control.explain()
