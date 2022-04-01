import pickle
import hashlib
import numpy as np


def get_pickle(file_name):
    with open(file_name, 'rb') as f:
        return pickle.load(f)


def test1():
    t = get_pickle('q1.pickle')
    r = len(t.get_title())
    s = len(t.get_xlabel())
    x = len(t.get_ylabel())
    y = len(t.get_legend_handles_labels()[1])
    a = len(t.get_xticks())
    b = len(t.get_yticks())
    if r > 0 and s > 0 and x > 0 and y == 1 and a > 0 and b > 0:
        res = True
    else:
        res = False
    assert res


def test2():
    t = get_pickle('q2.pickle')
    r = len(t.get_title())
    s = len(t.get_xlabel())
    x = len(t.get_ylabel())
    a = len(t.get_xticks())
    b = len(t.get_yticks())
    if r > 0 and s > 0 and x > 0 and a > 0 and b > 0:
        res = True
    else:
        res = False
    assert res


def test3():
    t = get_pickle('q3.pickle')
    r = len(t.get_title())
    s = len(t.get_xlabel())
    x = len(t.get_ylabel())
    y = len(t.get_legend_handles_labels()[1])
    a = len(t.get_xticks())
    b = len(t.get_yticks())
    if r > 0 and s > 0 and x > 0 and y == 3 and a > 0 and b > 0:
        res = True
    else:
        res = False
    assert res


def test4():
    t = get_pickle('q4.pickle')
    r = len(t.get_title())
    s = len(t.get_xlabel())
    x = len(t.get_ylabel())
    y = len(t.get_legend_handles_labels()[1])
    a = len(t.get_xticks())
    b = len(t.get_yticks())
    if r > 0 and s > 0 and x > 0 and y > 0 and a > 0 and b > 0:
        res = True
    else:
        res = False
    assert res


def test5():
    t = get_pickle('q5.pickle')
    r = len(t.get_title())
    s = len(t.get_xlabel())
    x = len(t.get_ylabel())

    if r > 0 and s > 0 and x > 0:
        res = True
    else:
        res = False
    assert res
