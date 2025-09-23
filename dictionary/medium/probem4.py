#Sort a dictionary by values and display the sorted result.

my_dict = {
    "praveen_age" : 36,
    "Ishani_age"  : 5,
    "sujata_age" : 30,
    }

sorted_dict = dict(sorted(my_dict.items(), key = lambda  item:item[1]))#sorting the dictionary
print(my_dict)#print origanal dictionary
print (sorted_dict)#print sorted dictionary