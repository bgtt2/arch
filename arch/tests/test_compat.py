import pytest
import numpy as np
from arch.compat.numba import PerformanceWarning

try:
    import numba  # noqa: F401

    HAS_NUMBA = True
except ImportError:
    HAS_NUMBA = False

from arch.univariate.recursions_python import arch_recursion


@pytest.mark.skipif(HAS_NUMBA, reason='Can only test when numba is not available.')
def test_performance_warning():
    parameters = np.array([1, .1])
    nobs = 100
    resids = np.ones(nobs)
    sigma2 = resids.copy()
    p = 1
    backcast = 1.0
    var_bounds = np.empty((nobs, 2))
    var_bounds[:, 0] = 0.0
    var_bounds[:, 1] = 1.0e14
    with pytest.warns(PerformanceWarning):
        arch_recursion(parameters, resids, sigma2, p, nobs, backcast, var_bounds)
