# Convert a list of tuples into a dictionary. require list knowledge  [(a,1),(b,2)] => {a:1,b:2}
list_of_tuples = []  #intializing list
n = int(input("enter the range of list: "))  #taking input as range of list
for _ in range(n):  #loop to create list in defined range
    a = input("enter the key value: ")  #taking input as key
    b = int(input("enter the values: "))  #taking input as value
    tuples = (a, b)  #forming tuples
    list_of_tuples.append(tuples)  #adding tuples to list
print("list of tuples is :", list_of_tuples)  #printing the list of tuples  
dictionary = dict(list_of_tuples)  #converting list of tuples to dictionary
print("dictionary is :", dictionary)  #printing the dictionary