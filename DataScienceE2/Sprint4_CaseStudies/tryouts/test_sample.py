import pickle
import hashlib
import pytest
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def get_pickle(covid19):
    with open(covid19,'rb')as f:
        while True:
            try:
                obj = pickle.load(f)
                return obj
            except EOFError:
                print('Done')
                break

def hashit(obj):
        obj = str(obj).encode()
        m = hashlib.md5()
        m.update(bytes(obj))
        return m.hexdigest()
    
    
def test1():
    A1 = get_pickle('A1.pickle')
    assert hashit(A1) == '1a6495e2535a6baf39f27ecede1c67a0'
    
def test2():
    A2 = get_pickle('A2.pickle')
    assert hashit(A2[0]) == '5e875732345f885cdd1c7e199e58f909'
    
def test3():
    A3 = get_pickle('A3.pickle')
    assert hashit(A3[-1]) == 'c20ad4d76fe97759aa27a0c99bff6710'
    
def test4():
    A4 = get_pickle('A4.pickle')
    assert hashit(A4[4]) == '0dabe12382064d1755527312fbca6a09'
    
def test5():
    A5 = get_pickle('A5.pickle')
    assert hashit(A5.get_size_inches()) == '69f9c8a184caa21881441c9d196240aa'
    