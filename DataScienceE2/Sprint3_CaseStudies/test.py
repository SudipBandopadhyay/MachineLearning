import pickle

def get_file(file_name):
    with open(file_name, "rb") as fp:
        data = pickle.load(fp)
        return data

income_confusion = get_file("Confusion_Matrix.txt")
income_acc = get_file("Accuracy.txt")
income_roc = get_file("ROC-Score.txt")
income_f1_macro = get_file("F1-Score-Macro.txt")
income_specificity = get_file("Specificity.txt")
income_sensitivity = get_file("Sensitivity.txt")

income_confusion = income_confusion.ravel()


score = 0
if((income_confusion[0]>=4500) and (income_confusion[3]>=1450) and (0.75 <= round(income_acc,2) <= 0.99)and (0.75 <= round(income_roc,2) <=0.99) and (0.70 <= round(income_f1_macro,2) <= 0.99) and (0.75 <= round(income_acc,2) <= 0.99) and (0.75 <= round(income_specificity,2) <= 0.99) and (0.75 <= round(income_sensitivity,2) <=0.99)): 
    score = score + 100
    print("Score" ,score)
    print("Sample Validations matches the expected output")
    
elif((income_confusion[0]>=4000) and (income_confusion[3]>=1200) and (0.60 <= round(income_acc,2) <= 0.99)and (0.60 <= round(income_roc,2) <=0.99) and (0.60 <= round(income_f1_macro,2) <= 0.99) and (0.60 <= round(income_acc,2) <= 0.99) and (0.60 <= round(income_specificity,2) <= 0.99) and (0.60 <= round(income_sensitivity,2) <=0.99)): 
    score = score + 50
    print("Score" ,score)
    print("Try to imporve your model")
    
else:
    score = 0
    print("Sample Validations does not match the expected output")