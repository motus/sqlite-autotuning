import numpy as np

FUNC_DOMAIN = (0, 1000000)
FUNC_RANGE = (0.2, 1.8)


# A popular synthetic target for optimization
def gramacy_lee(x: float) -> float:
    "Gramacy & Lee (2012) Function"
    return np.sin(10 * np.pi * x) / (2 * x) + (x - 1) ** 4


# Scale Gramacy-Lee function to look like our Redis trial data
def target_func(x: float) -> float:
    return (gramacy_lee(x * 2e-6 + 0.5) + 3.0) * 0.2

