import turtle
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=1.0, height=1.0)  # fullscreen mode

turtle1 = turtle.Turtle()


def rand_color():
    return str("#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)]))  # get random color


def confetti_piece():  # Draws individual piece of rectangle confetti
    angle = random.randint(1, 90)
    turtle1.color(rand_color())
    turtle1.begin_fill()

    l1 = random.randint(5, 20)
    l2 = l1 + random.randint(10, 15)

    turtle1.left(angle)

    for x in range(2):
        turtle1.left(90)
        turtle1.forward(l1)

        turtle1.left(90)
        turtle1.forward(l2)

    turtle1.end_fill()


def generate_confetti():
    turtle1.speed(1000)

    turtle1.penup()
    turtle1.goto(
        (random.randint(-int(wn.window_width() / 2), int(wn.window_width() / 2)),
         random.randint(-int(wn.window_height() / 2), int(wn.window_height() / 2))))  # assuming 1920 x 1080

    confetti_piece()

    """
    turtle1.pendown()

    turtle1.begin_fill()
    turtle1.color(rand_color())
    
    turtle1.circle(random.randint(15, 35))  # draw circle with random radius
    turtle1.end_fill()
    """


while True:  # infinite loop
    generate_confetti()

while True:
    pass
