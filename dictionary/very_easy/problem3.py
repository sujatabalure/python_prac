#Update a value of an existing key (e.g., change "age" from 20 to 25).
my_dict = { "name" : "sujata","age" : 30,"city" : "Pune"} #declare dictionary
print(my_dict) #before change
my_dict.update({"age" :25})#update original dictionary
print(my_dict) #after change
