import sys
sys.path.append(".")
from code.main import get_max, get_min, get_mean
import numpy as np

def test_max():
    x = np.arange(5)
    assert(get_max(x) == 4)

def test_min():
    x = [2, 4, 7, 3, 10]
    assert(get_min(x) == 2)

def test_mean():
    x = np.ones(10)
    assert(get_mean(x) == 1)
    
