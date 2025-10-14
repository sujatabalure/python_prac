# reverse dict with some added functionallity. this require list knowledge {a: 1, b : 1, c : 4}  =>  {1: [a,b], 4:c}
original_dictionary ={}     #intialzing dictionary
n = int(input("enter range of dictionary: "))  #taking input as range of dictionary
for _ in range(n):
    key = input("enter key value: ")  #taking input as key
    values = int(input("enter values: "))  #taking input as value
    original_dictionary [key] = values #forming dictionary
print(original_dictionary) #printing the dictionary

#after printing dictionary
reversed_dict = {}  #intialzing dictionary
for key, value in original_dictionary.items():
   if value not in reversed_dict:   #checking if the key is available in reverse dictionary 
    reversed_dict[value] = [key]    #add key in reverse dic 
   else:
    reversed_dict[value].append(key) #if val available in reverse dictionary add them in exsting key

print(reversed_dict)   #printing revresed dictionary