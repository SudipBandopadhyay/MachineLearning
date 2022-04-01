from testclustering import kmeans as kmeanstest

obj = kmeanstest.Answer()

passed_testcases = 0
total_questions = 7
failed_questions = ""

if obj._Answer__get_ans("kc_1a") == "c9aabeff5b67c40e1ded87c010e5be80" and obj._Answer__get_ans("kc_1b") == "cfcd208495d565ef66e7dff9f98764da":
    passed_testcases += 1
else:
    failed_questions += "Question No: {0} has failed to pass test cases\n".format(1)

if obj._Answer__get_ans("kc_2") == "f888ac49f1ca29ebfe7f7d9f45774903":
    passed_testcases += 1
else:
    failed_questions += "Question No: {0} has failed to pass test cases\n".format(2)

if obj._Answer__get_ans("kc_3") == "7484547d9a64de5a094fb01dcd8cb78a":
    passed_testcases += 1
else:
    failed_questions += "Question No: {0} has failed to pass test cases\n".format(3)

if obj._Answer__get_ans("kc_4") == "a3aa139870c552bab33053cf2cef0ce8":
    passed_testcases += 1
else:
    failed_questions += "Question No: {0} has failed to pass test cases\n".format(4)

if obj._Answer__get_ans("kc_5") == "d4696c0ab87943d26f6d09b7821eb4de":
    passed_testcases += 1
else:
    failed_questions += "Question No: {0} has failed to pass test cases\n".format(5)

if obj._Answer__get_ans("kc_6a") == "f827cf462f62848df37c5e1e94a4da74" and obj._Answer__get_ans(
        "kc_6b") == "9a9a81b80487607821684074d6d7dbf0":
    passed_testcases += 1
else:
    failed_questions += "Question No: {0} has failed to pass test cases\n".format(6)

if obj._Answer__get_ans("kc_7a") == "c4ca4238a0b923820dcc509a6f75849b" and obj._Answer__get_ans(
        "kc_7b") == "cfcd208495d565ef66e7dff9f98764da":
    passed_testcases += 1
else:
    failed_questions += "Question No: {0} has failed to pass test cases\n".format(7)

print("=============================== Kmeans Clustering TEST Result  =============================")
print("{0} questions are passed successfully out of {1}".format(passed_testcases, total_questions))
print(failed_questions)