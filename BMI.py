# Author: Angie Dowdell
# Purpose: BMI Loop
# Date: February 23, 2016


#Welcome
print("Welcome to the BMI calculator!")


#Totals/ Set variables

totalHeight=0
totalWeight=0
totalBMI=0

#User Count
userCount=0

#User input

userInput=input("Press any key to continue or type q to quit: ")

while (userInput != "q") and (userInput != "Q"):
    name=input("Type in your name, please: ")

    weight = eval(input ("Enter your weight (in pounds): "))
    totalWeight= totalWeight + weight
    
    height = eval(input ("Enter your height (in inches): "))
    totalHeight=totalHeight + height
    
    
    BMI= 703 * (weight/((height)**2))
    BMI_float= format(BMI,'0.4f')
    totalBMI=totalBMI + BMI

    print(name, "your BMI is", BMI_float)

    userCount= userCount + 1

    userInput=input("Press any key to continue or type q to quit: ")
    

#Calculate Averages

print ("You calculated BMI for", userCount, "people.")
avg_weight= totalWeight/ userCount

print("The average weight is", avg_weight, "pounds.")


avg_height= totalHeight/ userCount

print("The average height is", avg_height, "inches.")

avg_BMI= totalBMI/ userCount

avg_BMI_float= format(avg_BMI, '0.4f')

print("The average BMI is "+ avg_BMI_float+ ".")

print("Goodbye!")



