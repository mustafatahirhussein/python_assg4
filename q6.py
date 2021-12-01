# Write a Python script to check if a given key already exists in a dictionary

dict_ex = {
    'a': "Pakistan", 'b': "Iran", 'c': "Turkey"
}

a = input("Enter key to search: ")

val = a
print(dict_ex.get(val, "Not found value " + val))
