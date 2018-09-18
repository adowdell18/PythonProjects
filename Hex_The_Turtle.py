# Purpose: Program uses Turtle graphics to draw a polygon
# File name: Dowdell_A_assignment03.py
# Angie Dowdell
# Date: February 13, 2016

# Create turtle Alicia
import turtle

alicia= turtle.Turtle()


alicia.pendown()

# Determine Dimensions of Polygon

polygonSideLength=eval(input("What is the side length of your polygon? "))
print ("Length of polygon side = ", polygonSideLength)
numberOfSides= 5 + (909329521%4)
print ("Number of polygon sides = ", numberOfSides)
turnAngle= 360 / numberOfSides
print ("Turn angle at each vertex = ", turnAngle)

# Set random fill color
import random

randomColor= random.randint(0,5)

if randomColor==0:
    alicia.fillcolor("red")
    print ("Random fill color is red" )

elif randomColor==1:
    alicia.fillcolor("green")
    print ("Random fill color is green" )
elif randomColor==2:
    alicia.fillcolor("blue")
    print ("Random fill color is blue" )
elif randomColor==3:
    alicia.fillcolor("cyan")
    print ("Random fill color is cyan" )
elif randomColor==4:
    alicia.fillcolor("magenta")
    print ("Random fill color is magenta" )

alicia.goto(0,0)
alicia.pen(pencolor="black", pensize=10)
alicia.pensize(25)

alicia.begin_fill()


# Drawing Sides of Polygon
for numberOfSides in range (0,numberOfSides):
    alicia.forward(polygonSideLength)
    alicia.left(turnAngle)
alicia.end_fill()
alicia.penup()




# Position Alicia and Write Label
alicia.setheading(270)
alicia.goto(50,-10)
alicia.penup()
alicia.forward(65)
alicia.left(90)
alicia.pendown()
alicia.write("Hexagon Drawn by Angie Dowdell", align = "center", font=("Arial", 12,
"normal"))
alicia.hideturtle()

turtle.done()

    







    
