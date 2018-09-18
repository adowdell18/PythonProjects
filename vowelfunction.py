def numLet(word):
    return len(word)

def numVowels(word):
    vowels=0
    for i in 'aeiou':
        vowels=vowels+1

    return(vowels)

def percVowels(word):
    return ((numVowels(word)/numLet(word))*100)
    


w='elephant'

##numLet(word)
##
##numVowels(word)
##
##percVowels(word)

print (numLet(w))                                                                                              
print(numVowels(w))

print(percVowels(w),'%')



##x='word'
##
##print(len(x))
