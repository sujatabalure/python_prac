# Calculate the product of all values in a dictionary with numeric values. {a =1, b=2, c=5}  ans 1*2*5 = 10
dictionary ={} #initilazing dictionary
n = int(input("enter the range of dictionary:  3")) #taking n as number of input elements for dictionary
for _ in range(n): #applying for loop to enter elements of dictionary until given range
    key = input("key: ")    #taking key inputs
    values = int (input ("values(number): ") )#taking values inputs
    dictionary [key]= values #forming dictionary from given input
print(dictionary) #printing the dictionary outside the loop4
product =1  #declaring a variable
for value in dictionary.values():   #applying for loop only for values of dictionary
    product *= values   #multiplying values to variable product 
print("product of dictionary values is ", product) # printing the product of values from dictionary 

