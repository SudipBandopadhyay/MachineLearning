import pickle
import hashlib


def usrans(filename):
    with open(filename, 'r') as f:
        return f.read()



def hashit(obj):
    obj = str(obj).encode()
    m = hashlib.md5(bytes(obj))
    m.update(bytes(obj))
#     print(m.hexdigest())
    return m.hexdigest()

def test_eda(usrans, expected):
    assert hashit(usrans) == expected


if __name__ == "__main__":
    
    test_details = [("submit2.txt",'8112e9c925ca6482a4321464412f9a86'),
                    ("submit3.txt",'2c73626eff0c715cd8c46430f1de9492'),
                    ("submit.txt",'b9fb3c55acb59b4b1834435190cd9154')]
    
    no_test_passed = 0
    no_test_failed = 0

    total_testcases = len(test_details)
    for i in test_details:
        try: 
            test_eda(usrans(i[0]), i[1])

            no_test_passed += 1
        except AssertionError:
            no_test_failed += 1
        except Exception:
            no_test_failed +=1

    if(no_test_failed +  no_test_passed) == total_testcases:
        score = (no_test_passed / total_testcases) * 100
        print("FS_SCORE:{0}%".format(score))
    else:
        print("FS_SCORE:0%")