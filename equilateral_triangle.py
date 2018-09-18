#Author: Angie Dowdell
#Program Description: Draws an equilateral triangle
#Date: February 4, 2016

x_first = int(input("enter the x value for the first point :"))
y_first = int(input("enter the y value for the first point :"))
x_second = int(input("enter the x value for the second point :"))
y_second = int(input("enter the y value for the second point :"))
x_third = int(input("enter the x value for the third point :"))
y_third = int(input("enter the y value for the third point :"))

import turtle
turtle.setup(425, 425)

alicia = turtle.Turtle()

alicia.penup()

alicia.goto(x_third,y_third)

alicia.pendown()

alicia.goto(x_first,y_first)


alicia.goto(x_second,y_second)

alicia.goto(x_third,y_third)




turtle.done()
 
