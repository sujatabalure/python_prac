#Find the key with the maximum value in a dictionary.
my_dict = {
    "praveen_age" : 36,
    "Ishani_age"  : 5,
    "sujata_age" : 30,
    }

max_age = max(my_dict.items(), key = lambda  item:item[1])
print(max_age)

