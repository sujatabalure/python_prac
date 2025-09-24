#Update a value of an existing key (e.g., change "age" from 20 to 25).
my_dict = { "name" : "sujata","age" : 30,"city" : "Pune"} #declaringdictionary
print(my_dict)  #printing the dictionary before updating
my_dict.update({"age" :25}) #updating original dictionary key age value to 25 from 20
print(my_dict) #printing the dictionary after updating
