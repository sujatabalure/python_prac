#Merge two dictionaries into one (e.g., using update()).
my_dict = { "name" : "sujata","age" : 30,"city" : "Punee"}  #declaring dictionary
print("old dictionary", my_dict)  #printing old dictionary
my_new_dict ={"name1" : "Ishani","age1" : 6, "city" : "Punee"}  #declaring new dictionary
my_dict.update(my_new_dict)  #merging dictionary
print("new dict", my_new_dict)   #printing new dictionary
print("merged dict ", my_dict)  #printing merged dictionary