import pickle
import hashlib
import numpy as np


def get_pickle(file_name):
    with open(file_name, 'rb') as f:
        return pickle.load(f)


def test1():
    t = get_pickle('q1b.pickle')
    u = ["Winner Winner Chicken Dinner"]

    assert type(t) == type(u)


def test2():
    x = 0
    y = 0

    t = get_pickle('q2b.pickle')

    r = t.shape
    if r==(1200,16):
        x=1

    cl = t.columns.tolist()
    cl.sort()
    t = ['LDAPS_CC1', 'LDAPS_CC2', 'LDAPS_CC3', 'LDAPS_CC4', 'LDAPS_LH', 'LDAPS_PPT1', 'LDAPS_PPT2', 'LDAPS_PPT3', 'LDAPS_PPT4', 'LDAPS_RHmax', 'LDAPS_RHmin', 'LDAPS_Tmax_lapse', 'LDAPS_Tmin_lapse', 'LDAPS_WS', 'Present_Tmax', 'Present_Tmin']
    if cl==t:
        y=1

    if x==1 and y==1:
        res=True
    else:
        res=False
    assert res



def test3():
    t = get_pickle('q3b.pickle')

    ulist = []
    for i in t:
          if i not in ulist:
              ulist.append(i)

    assert len(ulist) == 48



def test4():
    t = get_pickle('q4b.pickle')
    u = ["Winner Winner Chicken Dinner"]

    assert type(t) == type(u)


def test5():
    t = get_pickle('q5b.pickle')
    r = t.shape

    assert r == (1200,25)



