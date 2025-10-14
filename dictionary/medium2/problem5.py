# Merge three or more dictionaries. take dictionary as input and also no of dictonary as input
range_Dict = int(input("enter the number of dictionary range"))
dict_list =[]

for _ in range(range_Dict):
    n = int(input("enter range of dictionary"))
    dictionary ={}
    for _ in range(n):
        key =input ("enter the key value ")
        values = input (" enter the values ")
        dictionary [key] = values
    dict_list.append(dictionary)
#print(len(dict_list))

for i, dictionaries in enumerate(dict_list, 1):
    print(f"Dictionaries {i}: {dictionaries}") 

merge = {}
for d in dict_list:
    merge.update(d)
print("merged dictionary is :", merge)


