# Write a program to identify duplicate values from list.

list1 = ["ltr","mg","sq","kl","kg","ltr"]

duplicateVal = []

for i in list1:
    if i not in duplicateVal:
        duplicateVal.append(i)
    else:
        print(i,end=" ")



