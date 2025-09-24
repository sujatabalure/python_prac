#Copy a dictionary (using copy()) and show that modifying the copy doesn’t affect the original.
my_dict = { "name" : "sujata","age" : 30, "city" : "Punee"} #declaring dictionary
my_new_dict = my_dict.copy() #coping above dictionary to new dictionary
print(my_dict)  #printing original dictionary
print(my_new_dict)  #printing copied dictionary

my_new_dict = { "color" : "white"}  #modifying copied  dictionary
print (my_new_dict) #printing modified dictionary
print (my_dict)  #printing original dictionary


   