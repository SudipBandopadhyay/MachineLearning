import pickle
import pytest
import hashlib


def get_pickle(filename):
    with open(filename,'rb')as f:
        obj = pickle.load(f)
        return obj

    
def test1():
    A1 = get_pickle('house_df.pickle')
    assert A1==21613
    
def test2():
    A2 = get_pickle('desc.pickle')
    assert A2==[3.37, 0.23, 3.41]
    
def test3():
    A3 = get_pickle('Xshape.pickle')
    assert A3==19
    
def test4():
    A4 = get_pickle('yshape.pickle')
    assert A4==21613
    
    
def test5():
    A5 = get_pickle('Xtrain.pickle')
    assert A5==17290 
    
def test6():
    A6 = get_pickle('Xtest.pickle')
    assert A6==4323
    
    
        
    

