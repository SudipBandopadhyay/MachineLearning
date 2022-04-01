import pickle
import hashlib
import numpy as np


def get_pickle(file_name):
    with open(file_name, 'rb') as f:
        return pickle.load(f)


def test1():
    t = get_pickle('q1.pickle')
    r = np.round(t[9], 2)
    a = 83.42
    g = [5, 4, 3, 2, 1, 0]
    if a == r and type(t) == type(g):
        res = True
    else:
        res = False
    assert res


def test2():
    s = get_pickle('q2.pickle')
    
    x = 0

    for i in range(0,25):
        if s[i][1] != '26-07-13':
            x=1

    if x == 0:
        res = True
    else:
        res = False
    assert res


def test3():
    t = get_pickle('q3.pickle')
    assert t.shape == (1200, 25)
