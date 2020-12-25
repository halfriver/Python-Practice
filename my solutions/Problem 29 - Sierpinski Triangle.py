'''
Problem 29 - Sierpinski Triangle
- Create and visualize a fractal generator that forms a standard Sierpinski
triangle given a user-provided ***depth*** for which the fractal should be
generated.
- Hint: perform this using recursive calls.
'''

import turtle
import math


class TooDamnHighError(Exception):
    pass


class ZeroError(Exception):
    pass
        

# input/error handling
depth = input("What depth should the Sierpinski triangle be drawn to?\n").replace(" ", "")
while True:
    try:
        depth = int(depth)-1
        if depth > 8:
            raise TooDamnHighError()
        elif depth < 0:
            raise ZeroError
        break
    except ValueError:
        depth = input("Please input a whole number.\n")
    except TooDamnHighError:
        depth = input("Don't kill your machine Try again.\n")
    except ZeroError:
        depth = input("Please input a number greater than 0.\n")

# setup for turtle
angle = 60
length = 500
offset = 25
turtle.screensize(length+offset*2, length+offset*2)
turtle.setworldcoordinates(0, 0, length+offset*2, length+offset*2)
pen = turtle.Turtle()
pen.speed(0)


# given parent triangle's coordinates and length, return grandchildren starting points
def midpoints(parent_midpoint, parent_length):
    height = math.sin(math.radians(angle))*parent_length
    x = parent_midpoint[0]
    y = parent_midpoint[1]
    
    return [(x+(parent_length/4), y+(height/2)),
            (x-(parent_length/4), y-(height/2)),
            (x+(parent_length*3/4), y-(height/2))]


def sierpinski(midlist, length, depth):
    if depth != 0:
        for point in midlist:
            sierpinski(draw(point, length/2), length/2, depth-1)


def draw(parent_midpoint, parent_length):
    x = parent_midpoint[0]
    y = parent_midpoint[1]
    
    pen.up()
    pen.setposition(x, y)
    pen.setheading(0)
    pen.down()
    for side in range(3):
        pen.forward(parent_length/2)
        pen.right(angle*2)
    pen.up()

    return midpoints((x, y), parent_length/2)


# draw initial iteration
x = offset
y = offset

pen.up()
pen.setpos(x, y)
pen.down()
pen.forward(length)
for i in range(2):
    pen.left(angle*2)
    pen.forward(length)
pen.up()

height = math.sin(math.radians(angle))*length
x += length/4
y += height/2

sierpinski(draw((x, y), length), length, depth)

turtle.done()






