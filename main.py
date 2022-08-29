import numpy as np


def get_max(array):
    return np.amax(array)

def get_min(array):
    return np.amin(array)

def get_mean(array):
    return np.mean(array)



print("Hello World!")


def test_max():
    x = np.arange(5)
    assert(get_max(x) == 4)

def test_min():
    x = [2, 4, 7, 3, 10]
    assert(get_min(x) == 2)

def test_mean():
    x = np.ones(10)
    assert(get_mean(x) == 1)
    
