"""
Written by: Denis Chechulin
Date: Nov 1, 2024
"""

import turtle

# Create turtle
t = turtle.Turtle()

while True:
    # Create prompt
    s = int(input("Enter the length of the side of the square: "))

    # Clear the drawing and reset the turtle position
    t.clear()
    t.penup()
    t.goto(0, 0)
    t.setheading(0)
    t.pendown()

    # Draw a square
    for _ in range(4):
        t.forward(s)
        t.left(90)

