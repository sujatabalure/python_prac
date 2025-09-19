#Invert a dictionary (keys → values, values → keys).
my_dict = {
    "praveen" : 1,
    "Ishani"  :2,
    "sujata" : 3,
    }

inverted_dict = {value: key for key, value in my_dict.items()}
print(inverted_dict)

