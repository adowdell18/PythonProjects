#Angie Dowdell
#April 24, 2016

userInputAlpha=input('Enter the beginning year("q" or "Q" for quit): ')

while int(userInputAlpha)<1942 or int(userInputAlpha)>2014 or userInputAlpha.isdigit()==False:
    userInputAlpha=input('Year must be in the range 1942 to 2014: ')


userInputOmega=input('Enter the ending year("q" or "Q" for quit): ')


while int(userInputOmega)<1942 or int(userInputOmega)>2014 or userInputOmega.isdigit==False:
    userInputOmega=input('Year must be in the range 1942 to 2014: ')

file=open('bestsellers.txt')


for line in file:
    for i in range(int(userInputAlpha),(int(userInputOmega)+1)):
        if str(i) in line:
            print(line)



    
