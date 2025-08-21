#Copy a dictionary (using copy()) and show that modifying the copy doesn’t affect the original.
my_dict = {
    "name" : "sujata",
    "age" : 30,
    "city" : "Punee"
}
my_dau_dict = my_dict.copy()
print(my_dict)
print(my_dau_dict)

my_dau_dict.update({ "color" : "white"})
print(my_dau_dict)

#{"name1" : "Ishani",
   