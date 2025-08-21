#Update a value of an existing key (e.g., change "age" from 20 to 25).
my_dict = {
    "name" : "sujata",
    "age" : 30,
    "city" : "Pune"
}
print(my_dict) #before change
my_dict.update({"age" :25})
print(my_dict) #after change
