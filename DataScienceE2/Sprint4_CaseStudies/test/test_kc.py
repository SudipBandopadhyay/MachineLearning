from testclustering import kmeans as kmeanstest

obj = kmeanstest.Answer()

passed_testcases = 0
total_questions = 5
failed_questions = ""

if obj._Answer__get_ans("kc_1") == "309db917fa5315d2fe3355e449937eab":
    passed_testcases += 1
else:
    failed_questions += "Question No: {0} has failed to pass test cases\n".format(1)

if obj._Answer__get_ans("kc_2") == "a3aa139870c552bab33053cf2cef0ce8":
    passed_testcases += 1
else:
    failed_questions += "Question No: {0} has failed to pass test cases\n".format(2)

if obj._Answer__get_ans("kc_3a") == "a87ff679a2f3e71d9181a67b7542122c" and obj._Answer__get_ans("kc_3b") == "9a9a81b80487607821684074d6d7dbf0":
    passed_testcases += 1
else:
    failed_questions += "Question No: {0} has failed to pass test cases\n".format(3)

if obj._Answer__get_ans("kc_4") == "d2cbb3fbf167acebe02ec575c60c422b":
    passed_testcases += 1
else:
    failed_questions += "Question No: {0} has failed to pass test cases\n".format(4)

if obj._Answer__get_ans("kc_5") == "cfcd208495d565ef66e7dff9f98764da":
    passed_testcases += 1
else:
    failed_questions += "Question No: {0} has failed to pass test cases\n".format(5)

print("=============================== Kmeans Clustering TEST Result  =============================")
print("{0} questions are passed successfully out of {1}".format(passed_testcases, total_questions))
print(failed_questions)