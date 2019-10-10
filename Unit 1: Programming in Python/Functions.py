import turtle

from tkinter import *

c = turtle.Turtle()  # set my turtle


def car(red=1, green=0, blue=0):
    # This is my red car

    c.color(red, green, blue)  # I did this as rgb: is set to 1, g and b are set to 0

    c.begin_fill()  # this means start filling the figure...

    c.forward(100)  # you know all of these commands

    c.left(90)

    c.forward(20)

    c.left(90)

    c.forward(20)

    c.right(90)

    c.forward(20)

    c.left(90)

    c.forward(60)

    c.left(90)

    c.forward(20)

    c.right(90)

    c.forward(20)

    c.left(90)

    c.forward(20)

    c.end_fill()  # and the figure is done being drawn so stop filling the color

    # now for the wheels...

    c.color(0, 0, 0)  # the wheels are black

    c.up()

    c.forward(10)  # pick the pen up and move forward 10

    c.down()

    c.begin_fill()

    c.circle(10)  # put the pen down and draw a circle with a radius of 10

    c.end_fill()

    # and the second wheel...

    c.setheading(0)

    c.up()

    c.forward(90)

    c.right(90)

    c.forward(10)

    c.setheading(0)  # pick the pen up and position the second wheel

    c.begin_fill()

    c.down()

    c.circle(10)

    c.end_fill()


car()

c.up()

c.setheading(180)  # face my pointer to the left

c.forward(200)  # move forward 200 steps

c.setheading(0)  # face my pointer to the 0 degree position

c.down()  # put the pen back down

car(0, 0, 1)  # draw another car

mainloop()  # pause for the user to view
