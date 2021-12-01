# Write a program to check if there is any numeric value in list using for loop.

test_list = ["abc", "def", "7674", "sfn", "a4577"]

for i in range(len(test_list)):

    if test_list[i].isnumeric():
        print("value found ", test_list[i])

