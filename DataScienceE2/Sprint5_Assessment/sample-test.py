import pytest
import pickle
import hashlib

def hashit(f):
    f = str(f).encode()
    m = hashlib.md5()
    m.update(bytes(f))
    return m.hexdigest()

def unpick(f):
    with open(f, 'rb') as f:
        db = pickle.load(f)
        f.close()
        return db
    


def test1():
    ans = unpick('words-lower.pickle')
    assert hashit(sorted(ans)[10:20]) == '583ea5faaf8296153b9eddaf849a64f8'
    
    

def test2():
    ans = unpick('bigram.pickle')
    assert hashit(ans[10:20]) == '7d628d27afc4909f5a0e8a0f200142ac'
    
    

def test3():
    ans = unpick('stop-removed.pickle')
    assert hashit(sorted(ans)[40:50]) == '2c6c3625128289053cf0b0fbd90ad344'
    
    

def test4():
    ans = unpick('porter_stemmed.pickle')
    assert hashit(sorted(ans)[:50]) == 'dccb40065791b007617e28244817aec9'
    
    
def test5():
    ans = unpick('words_lemmatized.pickle')
    assert hashit(sorted(ans)[:20]) == '8edf6f6a06d4c5d55912a07cec064b50'   
    
    
def test6():
    ans = unpick('pos_tagged.pickle')
    assert hashit(sorted(ans)[20:60]) == '285f0c275a2be48e51adacfea92eea63'
    
def test7():
    ans = unpick('vocabulary.pickle')
    assert hashit(sorted(ans.items())[10:15]) == 'edf8573f8def55488c17b3f5b3780826'
  
    
def test8():
    ans1 = unpick('sentiment.pickle')
    assert hashit(ans1[1:3]) == 'ac474043b7710ff7b8dbf2afe1929685'
    
    