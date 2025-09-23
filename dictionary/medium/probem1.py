#Count word frequency in a string using a dictionary.
string = "send a code to git hub a"# declared a string
word_freq= {}#declared empty dictionary
word =string.split()#spliting the string and stored in word
for words in word: # added for loop to check words from string
    if words in word_freq :#checking words are present in dictionary or not
        word_freq [words] +=1 #increment the count if the word is present in dictionary
    else:
        word_freq [words] =1 
print (word_freq)#print dictionary