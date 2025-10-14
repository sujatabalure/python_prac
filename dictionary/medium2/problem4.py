# Update a dictionary with another dictionary only if keys don’t exist in the first dictionary. Merge dict1 in dict2 but only if key from dict 2 is not present in dict1
original_dictionary ={}     #intialzing dictionary
n = int(input("enter range of dictionary: "))  #taking input as range of dictionary
for _ in range(n):
    key = input("enter key value: ")  #taking input as key
    values = int(input("enter values: "))  #taking input as value
    original_dictionary [key] = values #forming dictionary
print(original_dictionary) #printing the dictionary

#duplicate dictionary
duplicate_dictionary= {}
n1= int(input("enter the range of dictionary "))
for _  in range(n1):
    key = input("enter the key ")
    values = input("enter the values ")
    duplicate_dictionary [key] = values
print (duplicate_dictionary)

for key , values in duplicate_dictionary.items():
    if key not in original_dictionary:
        original_dictionary[key] = duplicate_dictionary[key]
         
print(original_dictionary)





