#Copy a dictionary (using copy()) and show that modifying the copy doesn’t affect the original.
my_dict = { "name" : "sujata","age" : 30, "city" : "Punee"}#declaring dictionary
my_dau_dict = my_dict.copy()
print(my_dict)#printing original dictionary
print(my_dau_dict)#printing copied dictionary

my_dau_dict = { "color" : "white"}#modifying copied  dictionary
print (my_dau_dict)#printing modified dictionary
print (my_dict)#printing original dictionary

#{"name1" : "Ishani",
   