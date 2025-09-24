#Invert a dictionary (keys → values, values → keys).
my_dict = {
    "praveen" : 1,
    "Ishani"  :2,
    "sujata" : 3,
    }  #declaring dictionary

inverted_dict = {value: key for key, value in my_dict.items()}  #inverting values from key 
print(inverted_dict) #printing inverted dictionary

