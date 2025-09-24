#Find the key with the maximum value in a dictionary.
my_dict = {
    "praveen_age" : 36,
    "Ishani_age"  : 5,
    "sujata_age" : 30,
    }  #delaring dictionary

max_age = max(my_dict.items(), key = lambda  item:item[1])  #using get fuction to find max value from dictionary
print(max_age)  #printing max value from dictionary

