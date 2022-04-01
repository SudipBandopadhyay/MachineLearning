import pickle
import numpy as np


def get_pickle(file_name):
    with open(file_name, 'rb') as f:
        return pickle.load(f)


def test1():
    t = get_pickle('q1b.pickle')
    g = 55
    assert type(t) == type(g)


def test2():
    t = get_pickle('q2b.pickle')
    g = 4096.6
    result = False
    if type(t) == type(np.float64(65.43)):
        result = True
    elif type(t) == type(g):
        result = True
    assert result


def test3():
    t = get_pickle('q3b.pickle')
    g = [12.3456, 987.654]
    assert type(t) == type(g)


def test4():
    t = get_pickle('q4b.pickle')
    g = ["fgdhfhf", 1.234]
    assert type(t) == type(g)


def test5():
    t = get_pickle('q5b.pickle')
    g = 55
    assert type(t) == type(g)
