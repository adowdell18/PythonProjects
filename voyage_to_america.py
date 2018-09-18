import turtle

import math

import random

#Add title to the graphics window 		[turtle.title ()]

turtle.title ('Angie Dowdell')

#Setup screen size to create 800x800 ocean 	[turtle.setup (800, 800)]

turtle.setup (800, 800, 0, 0)

#Set background color 			[turtle.bgcolor()]

turtle.bgcolor("#00ff99")

#Pendown

turtle.pendown()


#Draw trash vortex at center of ocean (filled circle at (0,0) with radius 50)[turtle.circle(),turtle.fillcolor(),turtle.begin_fill(), turtle.end_fill()]

turtle.goto(0,0)
turtle.fillcolor("black")
turtle.begin_fill()

turtle.circle(50)




turtle.end_fill()
turtle.penup()

turtle.hideturtle()

#Create two turtle objects and initialize their states (color, visibility etc)	[turtle.Turtle()]



turtle1= turtle.Turtle()
turtle1.shape("turtle")
turtle1.color("purple")


turtle2= turtle.Turtle()
turtle2.shape("turtle")
turtle2.color("yellow")
#Initialize Boolean variables to represent turtle status (alive, reachedAmerica)




turtle1Alive = True




turtle2Alive= True





turtle1ReachedAmerica= False



turtle2ReachedAmerica= False





#Initialize distances travelled to 0

turtle1Cor=turtle1.pos()
turtle2Cor=turtle2.pos()

xTurtle1=turtle1Cor[0]
yTurtle1=turtle1Cor[1]


xTurtle2=turtle2Cor[0]
yTurtle2=turtle2Cor[1]

distanceTravelledTurtle1=0
distanceTravelledTurtle2=0

distanceTurtle1FromVortex=0
distanceTurtle2FromVortex=0


distanceTravelledTurtle1=((xTurtle1-(-500))**2+(yTurtle1-50)**2)**(1/2)
distanceTravelledTurtle2=((xTurtle2-(-500))**2+(yTurtle2-50)**2)**(1/2)

distanceTurtle1FromVortex=((xTurtle1-0)**2+(yTurtle1-50)**2)**(1/2)
distanceTurtle2FromVortex=((xTurtle2-0)**2+(yTurtle2-50)**2)**(1/2)












#Set drawing color and speed			[turtle.speed()]

randomTurtle1Speed= random.randint(10,100)
randomTurtle2Speed= random.randint(10,100)
turtle.pencolor("yellow")

turtle.speed(10)

turtle1.speed(randomTurtle1Speed)
turtle2.speed(randomTurtle2Speed)

#Move  turtles to start position in Asia (middle left edge of screen)


turtle1.penup()

turtle1.goto(-500,50)

turtle1.pendown()


turtle2.penup()

turtle2.goto(-500,50)

turtle2.pendown()





while (turtle1Alive or turtle2Alive) and not (turtle1ReachedAmerica or turtle2ReachedAmerica):

    #If turtle1 is alive then generate  random heading and assign it to turtle1 (suggested range -60 to 60)w
    if turtle1Alive==True:
        randomHeadingTurtle1=random.randint(-60,60)
        turtle1.setheading(randomHeadingTurtle1)
    #Generate random distance and move turtle1 forward by this distance (suggested range 10 to 20)
        randomDistanceTurtle1=random.randint(10,30)
        turtle1.forward(randomDistanceTurtle1)
    #Generate random distance and move turtle2 forward by this distance (suggested range 10 to 20)
    if turtle2Alive==True:
        randomHeadingTurtle2=random.randint(-60,60)
        turtle2.setheading(randomHeadingTurtle2)
    #Generate random distance and move turtle2 forward by this distance (suggested range 10 to 20)
        randomDistanceTurtle2=random.randint(10,30)
        turtle2.forward(randomDistanceTurtle2)

   #Update distances travelled by turtle1 and turtle2

    turtle1Cor=turtle1.pos()
    turtle2Cor=turtle2.pos()

    xTurtle1=turtle1Cor[0]
    yTurtle1=turtle1Cor[1]


    xTurtle2=turtle2Cor[0]
    yTurtle2=turtle2Cor[1]
    
    distanceTravelledTurtle1=((xTurtle1-(-500))**2+(yTurtle1-50)**2)**(1/2)
    distanceTravelledTurtle2=((xTurtle2-(-500))**2+(yTurtle2-50)**2)**(1/2)

    distanceTurtle1FromVortex=((xTurtle1-0)**2+(yTurtle1-50)**2)**(1/2)
    distanceTurtle2FromVortex=((xTurtle2-0)**2+(yTurtle2-50)**2)**(1/2)
        
   #If turtle1 position is inside vortex then turtle1 is dead
 
 
    if distanceTurtle1FromVortex <=50:
        turtle1Alive=False
        
        
    

   #If turtle2 position is inside vortex then turtle2 is dead
    if distanceTurtle2FromVortex <=50:
        turtle2Alive=False
        
   #If turtle1 position is on or beyond right edge of window then turtle1 reached America
    
    

    if distanceTravelledTurtle1 >=700:
        turtle1ReachedAmerica=True
        

   #If turtle2 position is on or beyond right edge of window then turtle2 reached America
   
    
    if distanceTravelledTurtle2 >=700:
        turtle2ReachedAmerica=True
        
#End while loop

#Display distances travelled and final positions of turtle1 and turtle2

turtle1Cor=turtle1.pos()
turtle2Cor=turtle2.pos()

xTurtle1=int(turtle1Cor[0])
yTurtle1=int(turtle1Cor[1])


xTurtle2=int(turtle2Cor[0])
yTurtle2=int(turtle2Cor[1])
    
distanceTravelledTurtle1=int(((xTurtle1-(-500))**2+(yTurtle1-50)**2)**(1/2))
distanceTravelledTurtle2=int(((xTurtle2-(-500))**2+(yTurtle2-50)**2)**(1/2))

distanceTurtle1FromVortex=int(((xTurtle1-0)**2+(yTurtle1-50)**2)**(1/2))
distanceTurtle2FromVortex=int(((xTurtle2-0)**2+(yTurtle2-50)**2)**(1/2))


#Write Labels
turtle=turtle.Turtle()


turtle.penup()
turtle.goto(150,-150)
turtle.write('Total distance covered by turtle1: ' +str(distanceTravelledTurtle1), align = "left", font=("Arial", 12,"normal"))


turtle.penup()
turtle.goto(150,-170)
turtle.write('Total distance covered by turtle2: '+ str(distanceTravelledTurtle2), align = "left", font=("Arial", 12,"normal"))


turtle.penup()
turtle.goto(150,-190)
turtle.write('Final position of turtle 1: x= '+ str(xTurtle1)+', '+'y= '+ str(yTurtle1), align = "left", font=("Arial", 12,"normal"))


turtle.penup()
turtle.goto(150,-210)
turtle.write('Final position of turtle 2: x= '+ str(xTurtle2)+', '+'y= '+ str(yTurtle2), align = "left", font=("Arial", 12,"normal"))



    
#If turtle1 is not alive then display appropriate message

if turtle1Alive== False:
   
    turtle.penup()
    turtle.goto(150,-230)
    turtle.write("Turtle1 died in the trash vortex!", align = "left", font=("Arial", 12,"normal"))


#If turtle2 is not alive then display appropriate message
if turtle2Alive==False:
    
    turtle.penup()
    turtle.goto(150,-250)
    turtle.write('Turtle2 died in the trash vortex!', align = "left", font=("Arial", 12,"normal"))

#if both turtle1 and turtle2 reached America then display appropriate message

if turtle1Alive==True and turtle2Alive==True:
    
    turtle.penup()
    turtle.goto(150,-270)
    
    turtle.write("Both turtles managed to reach America!", align = "left", font=("Arial", 12,"normal"))



#else if turtle1 reached America then display appropriate message

elif turtle1ReachedAmerica==True:   
    turtle.penup()
    turtle.goto(150,-290)
    turtle.write("Only Turtle1 managed to reach America!", align = "left", font=("Arial", 12,"normal"))
    
#else if turtle2 reached America then display appropriate message

elif turtle2ReachedAmerica==True:
   
    turtle.penup()
    turtle.goto(150,-310)
    turtle.write("Only Turtle2 managed to reach America!", align = "left", font=("Arial", 12,"normal"))
turtle.hideturtle()









