#Create a dictionary with default values using fromkeys() (e.g., keys as subjects, default values "Not Assigned").
keys =["hindi" , "english","maths"] #decalring dictionary  with keys
default_values = "subject"     #declaring with default values
my_dict = dict.fromkeys(keys,default_values )  #by using fromkeys fucntion adding default values to all keys
print(my_dict)  #printing dictionary