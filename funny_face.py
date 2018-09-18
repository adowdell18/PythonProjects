#Author: Angie Dowdell
#Program name: DowdellL4.py
#Program Description: Draws a funny face
#Date: February 4, 2016


import turtle
turtle.penup()
turtle.goto(-100,0)
turtle.color("red", "yellow")
turtle.begin_fill()
turtle.forward(300)
turtle.right(160)
turtle.forward(100)
turtle.end_fill()
turtle.penup()
turtle.goto(-150, 150)
turtle.pendown()
turtle.color("black", "green")
turtle.begin_fill()
turtle.circle(45)
turtle.end_fill()
turtle.penup()
turtle.goto(150, 150)
turtle.pendown()
turtle.color("black", "green")
turtle.begin_fill()
turtle.circle(45)
turtle.end_fill()

turtle.penup()
turtle.goto (-10, 300)
turtle.pendown()
turtle.circle(270)

#Stick Body
turtle.penup()
turtle.goto(75,-225)
turtle.setheading(270)
turtle.pendown()
turtle.pensize(5)
turtle.color("black","black")
turtle.forward(90)


#Stick Arm (left)

turtle.penup()
turtle.goto(75,-250)
turtle.setheading(160)
turtle.pendown()
turtle.pensize(5)
turtle.color("black","black")
turtle.forward(50)


#Stick Arm (Right)

turtle.penup()
turtle.goto(75,-250)
turtle.setheading(20)
turtle.pendown()
turtle.pensize(5)
turtle.color("black","black")
turtle.forward(50)


#Stick Leg (left)

turtle.penup()
turtle.goto(75,-315)
turtle.setheading(200)
turtle.pendown()
turtle.pensize(5)
turtle.color("black","black")
turtle.forward(50)



#Stick Leg (Right)

turtle.penup()
turtle.goto(75,-315)
turtle.setheading(340)
turtle.pendown()
turtle.pensize(5)
turtle.color("black","black")
turtle.forward(50)
turtle.done




