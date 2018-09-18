#Angie Dowdell
#February 18, 2016


# Welcome!
print("Welcome to the Amazing character generator!")

#Let's make a few choices about your character!

userNum= eval(input("Enter a number between 1 and 30: "))

userLet=input("Enter a letter a, b, or c: ")

characterName= input("Enter a name for your character: ")

#Retrieve Random Number

import random

randomNum= random.randint(1,3)

# Character's Race

if (userNum >= 1) and (userNum <=10):
    race = ('elf')
    
elif (userNum >= 11) and (userNum <=20):
    race = ('dwarf')

elif (userNum >= 21) and (userNum <=30):
    race = ('human')

#Character's Gender

if userNum% 2==0:
    gender= ('female')

else:
    gender=('male')

# Character's Class


if userLet== ('a'):
    characterClass = ('fighter')
elif userLet== ('b'):
    characterClass = ('wizard')
elif userLet== ('c'):
    characterClass = ('cleric')

#Hit Points

hitPoints= 8 * randomNum

# Output the character generated

print(characterName +", the " + gender + ", " + race + ", "+ characterClass+ " has " + str(hitPoints) + " hit points!")

    




