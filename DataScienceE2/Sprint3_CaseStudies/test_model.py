import pickle
import hashlib


def usrans(filename):
    with open(filename, 'r') as f:
        return f.read()



def hashit(obj):
    obj = str(obj).encode()
    m = hashlib.md5(bytes(obj))
    m.update(bytes(obj))
    # print(m.hexdigest())
    return m.hexdigest()

def test_eda(usrans, expected):
    usrans = hashit(usrans)
    print(hashit(usrans),expected)
    assert hashit(usrans) == expected


if __name__ == "__main__":
    
    test_details = [("submit0.txt",'c0699cdb2419257d3617c913b89e9dae'),
                    ("submit1.txt",'311673e1e98f3872ba6c3b08e54da1fa'),
                    ("submit2.txt",'204168baf66095527fe0c7253d031677')]
    
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