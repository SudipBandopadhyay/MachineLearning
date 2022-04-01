import pytest
import pickle
import numpy as np


def get_pickle(file_name):
    with open(file_name, 'rb') as f:
        return pickle.load(f)


def test_s1():
    s1=get_pickle('S1.pickle')
    ss1=[3818, 3817, 3816, 3815, 3814, 3813, 3812, 3811, 3810, 3809]
    assert 'order' == s1.columns
    assert ss1 == list((s1.sort_values('order', ascending=False).iloc[:10]).order)
    

def test_s2():
    s2=get_pickle('S2.pickle')
    ss2={'abay': {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
 'abc': {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
 'abd': {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
 'abilities': {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
 'ability': {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
 'able': {0: 0, 1: 0, 2: 1, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
 'abode': {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
 'absolutely': {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
 'absolutly': {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
 'ac': {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}}
    assert ss2 == s2.iloc[:10,:10].to_dict()

def test_s3():
    s3=get_pickle('S3.pickle')
    ss3={'abay': {0: 0.0,  1: 0.0,  2: 0.0,  3: 0.0,  4: 0.0,  5: 0.0,  6: 0.0,  7: 0.0,  8: 0.0,  9: 0.0},
 'abc': {0: 0.0,  1: 0.0,  2: 0.0,  3: 0.0,  4: 0.0,  5: 0.0,  6: 0.0,  7: 0.0,  8: 0.0,  9: 0.0},
 'abd': {0: 0.0,  1: 0.0,  2: 0.0,  3: 0.0,  4: 0.0,  5: 0.0,  6: 0.0,  7: 0.0,  8: 0.0,  9: 0.0},
 'abilities': {0: 0.0,  1: 0.0,  2: 0.0,  3: 0.0,  4: 0.0,  5: 0.0,  6: 0.0,  7: 0.0,  8: 0.0,  9: 0.0},
 'ability': {0: 0.0,  1: 0.0,  2: 0.0,  3: 0.0,  4: 0.0,  5: 0.0,  6: 0.0,  7: 0.0,  8: 0.0,  9: 0.0},
 'able': {0: 0.0,  1: 0.0,  2: 0.058823529411764705,  3: 0.0,  4: 0.0,  5: 0.0,  6: 0.0,  7: 0.0,  8: 0.0,  9: 0.0},
 'abode': {0: 0.0,  1: 0.0,  2: 0.0,  3: 0.0,  4: 0.0,  5: 0.0,  6: 0.0,  7: 0.0,  8: 0.0,  9: 0.0},
 'absolutely': {0: 0.0,  1: 0.0,  2: 0.0,  3: 0.0,  4: 0.0,  5: 0.0,  6: 0.0,  7: 0.0,  8: 0.0,  9: 0.0},
 'absolutly': {0: 0.0,  1: 0.0,  2: 0.0,  3: 0.0,  4: 0.0,  5: 0.0,  6: 0.0,  7: 0.0,  8: 0.0,  9: 0.0},
 'ac': {0: 0.0,  1: 0.0,  2: 0.0,  3: 0.0,  4: 0.0,  5: 0.0,  6: 0.0,  7: 0.0,  8: 0.0,  9: 0.0}}
    assert ss3 == s3.iloc[:10,:10].to_dict()
    

def test_s4():
    s4=get_pickle('S4.pickle')
    ss4={'abay': {0: 0.0,  1: 0.0,  2: 0.0,  3: 0.0,  4: 0.0,  5: 0.0,  6: 0.0,  7: 0.0,  8: 0.0,  9: 0.0},
 'abc': {0: 0.0,  1: 0.0,  2: 0.0,  3: 0.0,  4: 0.0,  5: 0.0,  6: 0.0,  7: 0.0,  8: 0.0,  9: 0.0},
 'abd': {0: 0.0,  1: 0.0,  2: 0.0,  3: 0.0,  4: 0.0,  5: 0.0,  6: 0.0,  7: 0.0,  8: 0.0,  9: 0.0},
 'abilities': {0: 0.0,  1: 0.0,  2: 0.0,  3: 0.0,  4: 0.0,  5: 0.0,  6: 0.0,  7: 0.0,  8: 0.0,  9: 0.0},
 'ability': {0: 0.0,  1: 0.0,  2: 0.0,  3: 0.0,  4: 0.0,  5: 0.0,  6: 0.0,  7: 0.0,  8: 0.0,  9: 0.0},
 'able': {0: 0.0,  1: 0.0,  2: 0.24253562503633297,  3: 0.0,  4: 0.0,  5: 0.0,  6: 0.0,  7: 0.0,  8: 0.0,  9: 0.0},
 'abode': {0: 0.0,  1: 0.0,  2: 0.0,  3: 0.0,  4: 0.0,  5: 0.0,  6: 0.0,  7: 0.0,  8: 0.0,  9: 0.0},
 'absolutely': {0: 0.0,  1: 0.0,  2: 0.0,  3: 0.0,  4: 0.0,  5: 0.0,  6: 0.0,  7: 0.0,  8: 0.0,  9: 0.0},
 'absolutly': {0: 0.0,  1: 0.0,  2: 0.0,  3: 0.0,  4: 0.0,  5: 0.0,  6: 0.0,  7: 0.0,  8: 0.0,  9: 0.0},
 'ac': {0: 0.0,  1: 0.0,  2: 0.0,  3: 0.0,  4: 0.0,  5: 0.0,  6: 0.0,  7: 0.0,  8: 0.0,  9: 0.0}}
    assert ss4 == s4.iloc[:10,:10].to_dict()
    

def test_s5():
    s5=get_pickle('S5.pickle')
    ss5={'abay': {0: 0.0,  1: 0.0,  2: 0.0,  3: 0.0,  4: 0.0,  5: 0.0,  6: 0.0,  7: 0.0,  8: 0.0,  9: 0.0},
 'abc': {0: 0.0,  1: 0.0,  2: 0.0,  3: 0.0,  4: 0.0,  5: 0.0,  6: 0.0,  7: 0.0,  8: 0.0,  9: 0.0},
 'abd': {0: 0.0,  1: 0.0,  2: 0.0,  3: 0.0,  4: 0.0,  5: 0.0,  6: 0.0,  7: 0.0,  8: 0.0,  9: 0.0},
 'abilities': {0: 0.0,  1: 0.0,  2: 0.0,  3: 0.0,  4: 0.0,  5: 0.0,  6: 0.0,  7: 0.0,  8: 0.0,  9: 0.0},
 'ability': {0: 0.0,  1: 0.0,  2: 0.0,  3: 0.0,  4: 0.0,  5: 0.0,  6: 0.0,  7: 0.0,  8: 0.0,  9: 0.0},
 'able': {0: 0.0,  1: 0.0,  2: 0.19870987748911204,  3: 0.0,  4: 0.0,  5: 0.0,  6: 0.0,  7: 0.0,  8: 0.0,  9: 0.0},
 'abode': {0: 0.0,  1: 0.0,  2: 0.0,  3: 0.0,  4: 0.0,  5: 0.0,  6: 0.0,  7: 0.0,  8: 0.0,  9: 0.0},
 'absolutely': {0: 0.0,  1: 0.0,  2: 0.0,  3: 0.0,  4: 0.0,  5: 0.0,  6: 0.0,  7: 0.0,  8: 0.0,  9: 0.0},
 'absolutly': {0: 0.0,  1: 0.0,  2: 0.0,  3: 0.0,  4: 0.0,  5: 0.0,  6: 0.0,  7: 0.0,  8: 0.0,  9: 0.0},
 'ac': {0: 0.0,  1: 0.0,  2: 0.0,  3: 0.0,  4: 0.0,  5: 0.0,  6: 0.0,  7: 0.0,  8: 0.0,  9: 0.0}}
    assert ss5 == s5.iloc[:10,:10].to_dict()

def test_s6():
    s6=get_pickle('S6.pickle')
    ss6={'values': {'abay': 9.027476530860483,
  'abc': 9.027476530860483,
  'abd': 9.027476530860483,
  'abilities': 7.641182169740591,
  'ability': 5.891982314931332,
  'able': 4.364037436748415,
  'abode': 8.334329350300536,
  'absolutely': 5.416558618216257,
  'absolutly': 9.027476530860483,
  'ac': 7.928864242192372}}
    assert 'values' == s6.columns
    assert ss6 == s6.iloc[:10,:10].to_dict()