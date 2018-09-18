sentence="I am happy to meet you!"

target="happy"

replacement="glad"


i=0
N=""

while (i< len(replacement)):
    if target[i:len(replacement)]==replacement:
        i=i+len(replacement)
    else:
        N= N+replacement[i]
        print(i)
        i=i+1

print(N)

x=sentence.find(target)

print(x)

new_sentence=sentence[:sentence.find(target)]+ replacement + sentence[sentence.find(target)+len(target):]


print(new_sentence)
        

        
        
