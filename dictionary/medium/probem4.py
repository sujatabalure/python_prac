#Sort a dictionary by values and display the sorted result.

my_dict = {
    "praveen_age" : 36,
    "Ishani_age"  : 5,
    "sujata_age" : 30,
    }  #declaring dictionary

sorted_dict = dict(sorted(my_dict.items(), key = lambda  item:item[1])) #sorting the dictionary
print(my_dict) #printing origanal dictionary
print (sorted_dict) #printing sorted dictionary