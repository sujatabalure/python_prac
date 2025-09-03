#Count word frequency in a string using a dictionary.
string = "send a code to git hub a"
word_freq= {}
word =string.split()
for words in word:
    if words in word_freq :
        word_freq [words] +=1
    else:
        word_freq [words] =1
print (word_freq)