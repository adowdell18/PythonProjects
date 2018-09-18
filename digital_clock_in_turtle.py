from datetime import datetime
import time
import turtle
    

#Create a clock by drawing a rectangle

def createClock():
    turtleClock=turtle.Turtle()
    turtleClock.fillcolor("purple")
    turtleClock.pencolor("black")



    turtleClock.begin_fill()
    turtleClock.penup()
    turtleClock.goto(-100,-50)
    turtleClock.pendown()
    turtleClock.forward(200)    
    turtleClock.left(90)
    turtleClock.forward(100)
    turtleClock.left(90)
    turtleClock.forward(200)
    turtleClock.left(90)
    turtleClock.forward(100)
    turtleClock.end_fill()
    turtleClock.hideturtle()
    
    


#Retrieve current and previous times


def fetchTime():
    x=0
        
    while x==0:

        
        
##        current_time=datetime.datetime.strftime(datetime.datetime.now(), '%H:%M:%S')
##        previous_time = datetime.datetime.strftime(datetime.datetime.now(), '%H:%M:%S')

    # set previous time locally
        previous_time=datetime.now()
        
        previous_hour=previous_time.hour
     
        previous_minute=previous_time.minute

        previous_second=previous_time.second
    #set current time locally

        current_time=datetime.now()
        
        current_hour=current_time.hour
     
        current_minute=current_time.minute

        current_second=current_time.second

    #Create conditional  for retrieving time

        
        if current_time!= previous_time:
            previous_time=current_time
                    
            previous_hour=current_hour
     
            previous_minute=current_minute

            previous_second=current_second
            
        #Call writeTime function now that the current time has been retrieved
            
            writeTime()

            
            
            
            


#Create the window in which the clock will appear

def setupClockPanel():
    

    #Setup screen size to create clock panel

    turtle.setup (400, 400, 0, 0)

    #Set background color 			

    turtle.bgcolor("white")

    #Pendown

    turtle.pendown()
    turtle.hideturtle()

#Create a function that will write the time in window


def writeTime():

    time.sleep(1)
    

    turtle.clear()
    
    

    
    turtle.hideturtle()

    turtle.pencolor("#0000FF")
    

#Get Currrent Time

    current_time=datetime.now()
    
    current_hour=current_time.hour
    
    current_minute=current_time.minute
    
    current_second= int(current_time.second)
    
   
    


#Write Current Time on Clock Panel
    turtle.penup()
    turtle.goto(0,-20)
    turtle.pendown()
    
    turtle.speed(100)
    turtle.pencolor("#49E20E")
    turtle.write(str(current_hour)+':'+str(current_minute)+ ':'+ str(current_second), False, align="center", font=("Arial",25,"bold"))
    


#Create function to write name initials underneath clock


def writeName():
    name=turtle.Turtle()
    name.hideturtle()

    name.penup()
    name.goto(0,-75)
    name.pendown()

    name.pencolor("black")
    
    name.write("A.D.", False, align="center", font=("Arial",12,"bold"))

    
    

    
    

    


setupClockPanel()
createClock()
writeName()
fetchTime()





    
            

            
  
