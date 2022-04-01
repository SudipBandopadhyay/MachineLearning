import pickle
import hashlib
import pytest
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def get_pickle(FTSE):
    with open(FTSE,'rb')as f:
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
    assert hashit(A1) == '9ff2a8045acb45a174a0b3a5273e1eda'
    
    
def test2():
    A3 = get_pickle('A3.pickle')
    assert hashit(A3) == '9ff2a8045acb45a174a0b3a5273e1eda'
    
    
def test3():
    A6 = get_pickle('A6.pickle')
    assert hashit(type(A6)) == 'cc117bbc29a8650d24be9930295304d7'    
    
    
    
