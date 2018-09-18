
#Computing area of shell

import math

diameter_shell = eval(input("Enter the diameter of the turtle's shell (in inches): "))

radius_inches_shell = diameter_shell/2

radius_feet_shell= radius_inches_shell/12

area_shell =  (3.14* (radius_feet_shell)**2)/2

print("The area of the turtle's shell is ",area_shell, "in square feet")

#Computing area of head

diameter_head = eval (input("Enter the diameter of the turtle's head (in inches)): "))

radius_inches_head= diameter_head/2

radius_feet_head= radius_inches_head/12

area_head = (3.14 *(radius_feet_head)**2)

print("The area of the turtle's head is ", area_head, "in square feet.")
#Computing area of tail

tail_length = eval(input("Enter the length of one side of the tail (in inches): "))

tail_feet_length = tail_length/12
area_tail = (1/4) * (3)**1/2 * (tail_feet_length)**2
print("The area of the turtle's tail is ", tail_feet_length, "in square inches.")
#Computing area of leg

leg_length = eval(input("Enter the length of the turtle's leg (in inches): "))
leg_feet_length = leg_length/12

area_leg = leg_feet_length**2
area_legs = area_leg * 2
print("The total area of both legs is ", area_legs, "in square feet.")

#Computing area of entire turtle

area_turtle= area_shell + area_head + area_tail + area_legs
area_turtle_float = format(area_turtle,'0.2f')
print("The turtle's area is ", area_turtle_float, "square feet.")



#Calculating cost of paiting the turtle

paint_needed = area_turtle*0.10

paint_needed_float= format(paint_needed,'0.2f')

print ("You will need ", paint_needed_float, "gallons of paint.")


cost_paint = 20 * paint_needed

cost_paint_float = format(paint_needed,'0.2f')

print("It will cost $" ,cost_paint_float,"to repaint the turtle.")
