
from ._defaults_loader import DEFAULT_PREDICTION_TRACES, DEFAULT_FEATURE_TRACES, DEFAULT_BASE_CODE

class BaseTreeAdapter:
    """Base class for tree adapters.
    It implements the base code for the translation

    Args:
        feature_traces (list, optional): the featuretraces. Defaults to None, in which case the 
            default code ASP code will be used.
        prediction_traces (list, optional): the prediction traces. Defaults to None, in which case 
            the default code ASP code will be used.
        base_code (str, optional): the base code. Defaults to None, in which case the default code 
            ASP code will be used.
    """

    def get_logic_program(self, factor, prediction_traces=None, feature_traces=None, feature_names=None):
        """Returns the translation of the original decision tree as a logic program in a string.

        Returns:
            str: the translation as a string object.
        """
        if not hasattr(self, '_logic_program_translation'):
            translation = f'%%% thresholds\n{self._rule_per_leaf(factor)}\n' \
                f'%%% paths\n{self._thresholds(factor)}%\n' \
                f'%%% base\n{DEFAULT_BASE_CODE}%\n'
            if feature_traces is not None:
                translation += f'%%% feature traces\n{DEFAULT_FEATURE_TRACES}%\n'
            if prediction_traces is not None:
                translation += f'%%% prediction traces\n{DEFAULT_PREDICTION_TRACES}\n'
            if feature_names is not None:
                translation += f'%%% feature names\n{self._feature_names_rules(feature_names)}%\n'
            setattr(self, '_logic_program_translation', translation)
        print(getattr(self, '_logic_program_translation'))
        return getattr(self, '_logic_program_translation')

    def _rule_per_leaf(self, factor):
        raise NotImplementedError('This method must be implemented in the child class')

    def _thresholds(self, factor):
        raise NotImplementedError('This method must be implemented in the child class')

    def _feature_names_rules(self, feature_names):
        feature_name_rules = ''
        for i, f_name in enumerate(feature_names):
            feature_name_rules += f'feature_name({i},"{f_name}").\n'
        return feature_name_rules