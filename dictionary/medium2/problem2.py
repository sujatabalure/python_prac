#  Find all keys in a dictionary that correspond to a given value. {a:1, b:2, c:2} find 2 o/p is b,c
dictionary= {} #intializing dictionary
n = int(input("enter the range in numbers for dictionary: "))   #taking n as input range of dinctionary
for _ in range(n): #applying for loop to enter elements of dictionary until given range
    key = input("key: ")    #taking key inputs
    values = int (input ("values(number): ") )  #taking values inputs
    dictionary [key]= values    #forming dictionary from given input
print(dictionary)   #printing the dictionary outside the loop4

#after printing the dictionary
value_present_in_Dictionary = int(input("enter a value : "))    #taking input value to search in dictionary
matching_key = [key for key, values in dictionary.items()   #taking for loop to provide key from the dictionary as output
                if values == value_present_in_Dictionary]   #if the dictionary values matches with input value
       


if matching_key: #if matching key is present in the dictionary
    print ("key corresponding to the entered value " ,value_present_in_Dictionary,"for",matching_key) #printing key corresponding to value
else:
    print ("no corsponding keys are available for given input values")  #else print statement no keys are available