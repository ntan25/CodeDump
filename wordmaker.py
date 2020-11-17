import random

a = "string"

def wordmaker(word):

    for char in word: 
        newstring = ""
    
        if random.randint(0, 1) == 1: 
            char = char.upper()
            newstring += char
        else: 
            char = char.lower()
            newstring += char
    return newstring
    


print("This is working and the output is {}".format(wordmaker(a)))

