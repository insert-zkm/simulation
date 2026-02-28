import numpy as np


def uniform(size=None):
    return np.random.uniform(np.nextafter(0, 1), 1, size)


def choice(p):
    i = 0
    rnd = uniform() - p[0]

    while rnd >= 0:
        i += 1
        rnd = rnd - p[i]
    return i
