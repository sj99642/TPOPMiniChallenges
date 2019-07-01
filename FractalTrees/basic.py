"""
Draw a simple, perfectly self-similar tree, ideally using recursion.

Each branch splits off into 2 smaller branches, of half the length and
2/3 of the thickness, separated by 30 degrees. Go 6 layers deep.
"""

import turtle

def draw_simple_tree(start_heading, width, length, depth_remaining):
    turtle.setheading(start_heading)
    turtle.pensize(width)
    turtle.forward(length)

    if (depth_remaining > 1):
        draw_simple_tree(start_heading - 20, width * 0.75, length * 0.5, depth_remaining - 1)
        draw_simple_tree(start_heading + 20, width * 0.75, length * 0.5, depth_remaining - 1)
    
    turtle.setheading(start_heading)
    turtle.penup()
    turtle.backward(length)
    turtle.pendown()