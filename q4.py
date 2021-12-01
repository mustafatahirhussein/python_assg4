# Write a Python program to sum all the numeric items in a dictionary.

my_dict = {
    'a': '4574', 'b': 'abcd', 'c': '896', 'd': 'def'
}

totalSum = 0

for k in my_dict.keys():

    if my_dict[k].isnumeric():
        print("value found at Key", my_dict[k])
        totalSum = totalSum + int(my_dict[k])
print("total sum ", totalSum)
