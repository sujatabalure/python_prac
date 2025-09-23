#Create a dictionary with default values using fromkeys() (e.g., keys as subjects, default values "Not Assigned").
keys =["hindi" , "english","maths"]#initilazing with keys
default_values = "subject"#initilazing with default values
my_dict = dict.fromkeys(keys,default_values )#creating dictionary with default values
print(my_dict)#print dictionary