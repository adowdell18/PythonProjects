#Angie Dowdell
#Functions and Input Validation
#April 8, 2016


# Function accepts a parameter & returns a True or False value
def validInput(choice):
    while choice != 'x' and choice !='X'and choice != 'P' and choice !='V+' and choice != 'V-' and choice !='C+' and choice != 'C-' and choice != 'M' and choice !="0" and choice !="1" and choice !="2" and choice != "3" and choice !="4" and choice !="5" and choice != "6" and choice !="7" and choice != "8" and choice != "9" and choice !="10":
        choice=input("Please provide a valid choice: ")
    return choice
    



# Function accepts four parameters, updates and returns them

##def processChoice(choice, power, volume, channel):
def processChoice(choice, power, channel, volume):
    # Insert code for processing choice here

    #process choice for power
    if choice=="P":
        if power == "OFF":
            power="ON"
    ##            return on
        elif power == "ON":
            power="OFF"
    ##            return off

    #Process choice for increasing and decreasing volume
    if choice=="V-":
        volume=volume-1
        if volume<0:
            volume=1
    elif choice =="V+":
        volume=volume+1
        if volume>10:
            volume=10
    elif choice=="M":
        volume=0
    
        
    #Process choice for select channcel
    if choice=="1":
        channel=1
 
    elif choice=="2":
        channel=2
 
    elif choice=="3":
        channel=3
    
    elif choice=="4":
        channel=4

    elif choice=="5":
        channel=5

    elif choice=="6":
        channel=6

    elif choice=="7":
        channel=7

    elif choice=="8":
        channel=8

    elif choice=="9":
        channel=9
        
    elif choice=="10":
        channel=10
        
    #Process choice for increasing and decreasing channel

    if choice=="C-":
        channel=channel-1
        if channel<1:
            channel=10

    elif choice=="C+":
        channel=channel+1
        if channel>10:
            channel=1


    return power, channel, volume



def printTVState(power,channel, volume):

    print("TV is " + str(power)+ ", Channel: "+str(channel)+ " Volume level: "+str(volume))

   








    
def main():
##    Print information for user
    print("TV Remote Simulator")
    print("This program will allow you to turn the TV on and off; mute the TV; set the channel; increase and decrease the channel number and increase and decrease the volume level")
    print('Valid inputs: "P"(power), "V+/-" (volume up/down), "C+/-" (channel up/down), "M"(Mute), or channel number (range 1 to 10)')

##    Initialize power, channel and volume
    power= 'OFF'
    volume=1
    channel=1
    
##    Prompt user for choice
    choice=input("Please input your choice: ")

    validInput(choice)

    while choice !='x' and choice !='X':

        power, channel, volume=processChoice(choice, power, channel, volume)
        
        printTVState(power, channel, volume)
        
        choice=input("Please input your choice: ")


        validInput(choice)
    print('Thanks for using this app!')

        
        


main()
