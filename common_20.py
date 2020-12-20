import numpy as np
from itertools import product

all_transformations = tuple(product((0, 1, 2, 3), (0, 1)))

def transform(a: int, b: int, m: np.ndarray) -> np.ndarray:
    if a == 0:
        transformed = np.rot90(m)
    elif a == 1:
        transformed = np.rot90(np.rot90(m))
    elif a == 2:
        transformed = np.rot90(np.rot90(np.rot90(m)))
    else:
        transformed = m

    if b == 0:
        transformed = np.fliplr(transformed)

    return transformed
