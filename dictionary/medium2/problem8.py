# Check if two dictionaries are equal (same keys and values).
n = int(input("enter the range of first dictionary: "))  #taking input as range of first dictionary
dictionary1 ={} #intializing dictionary
for _ in range(n): #create the loop to take input in iterate manner
    key = input("enter the key: ") #taking key as input
    value = input ("enter the value: ") 
    dictionary1[key] = value
print(dictionary1)

n = int(input("enter range of 2nd dictionary: "))
dictionary2 = {}
for _ in range(n): #create the loop to take input in iterate manner
    key = input("enter the key: ")
    value = input ("enter the value: ")
    dictionary2[key] = value
print(dictionary2)

if(dictionary1 == dictionary2):
    print("dictionary1 and two has same keys and values")
else:
    print("dictionary1 and two do not have same values")

