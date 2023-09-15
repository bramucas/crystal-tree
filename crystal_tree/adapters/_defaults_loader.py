
from . import defaults_lp
try:
    import importlib.resources as pkg_resources
except ImportError:
    import importlib_resources as pkg_resources

_DEFAULT_PREDICTION_TRACES_LOCATION = "default_prediction_traces.lp"
DEFAULT_PREDICTION_TRACES = pkg_resources.read_text(defaults_lp, _DEFAULT_PREDICTION_TRACES_LOCATION)

_DEFAULT_FEATURE_TRACES_LOCATION = "default_feature_traces.lp"
DEFAULT_FEATURE_TRACES = pkg_resources.read_text(defaults_lp, _DEFAULT_FEATURE_TRACES_LOCATION)

_DEFAULT_BASE_CODE_LOCATION  = "default_extra.lp"
DEFAULT_BASE_CODE = pkg_resources.read_text(defaults_lp, _DEFAULT_BASE_CODE_LOCATION)
