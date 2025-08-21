#Merge two dictionaries into one (e.g., using update()).
my_dict = {
    "name" : "sujata",
    "age" : 30,
    "city" : "Punee"
}
my_dau_dict ={"name1" : "Ishani",
    "age1" : 6,
    "city1" : "Punee"

}
my_dict.update(my_dau_dict)
print(my_dict)