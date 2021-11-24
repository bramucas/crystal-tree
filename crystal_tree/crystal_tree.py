from crystal_tree.logic_tree import LogicTree

class CrystalTree():
    def __init__(self, dt, feature_names=None):
        self.logic_tree = LogicTree(dt, feature_names)
    
    def to_annotated_logic_program(self, paths="paths.lp", extra="extra.lp", traces="traces.lp"):
        if extra is not None:
            with open(extra, 'w') as extra_file:
                extra_file.write(self.logic_tree.extra)
        if traces is not None:
            with open(traces, 'w') as traces_file:
                traces_file.write(self.logic_tree.traces)
        if paths is not None:
            with open(paths, 'w') as paths_file:
                paths_file.write(self.logic_tree.get_paths())
    

