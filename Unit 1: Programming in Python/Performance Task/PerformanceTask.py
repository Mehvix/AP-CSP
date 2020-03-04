import turtle
import time
import random

delay = .1
score = 0

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")

board_size = 450
wn.setup(width=board_size, height=board_size)
wn.tracer(0)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
apple = turtle.Turtle()
apple.speed(0)
apple.shape("circle")
apple.color("green")
apple.penup()
apple.goto(0, board_size/5)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, (board_size/2)-40)
pen.write("Score: 0 ", align="center", font=("Courier", 24, "normal"))


def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# keeb
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

while True:
    wn.update()

    # Collision with the border
    if head.xcor() > (board_size/2 - 10) \
            or head.xcor() < -(board_size/2 - 10) \
            or head.ycor() > (board_size/2 - 10) \
            or head.ycor() < -(board_size/2 - 10):
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(board_size*2, board_size*2)
        segments.clear()

        # Reset
        score = 0
        delay = 0.1

        pen.clear()
        pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
        try:
            apple.goto(0, board_size / 5)
        except:
            pass

    if head.distance(apple) < 20:  # apple spawn

        x = random.randint(-(board_size/2) + 20, (board_size/2)- 20)
        y = random.randint(-(board_size/2) + 20, (board_size/2)- 20)

        """
        while True:
            for segment in segments:
                if not (((segment.xcor() - 20) < x < (segment.xcor() + 20)) and (segment.ycor() - 20) < y < (segment.ycor() + 20)):
                    continue
                x = random.randint(-(board_size / 2) - 10, (board_size / 2) - 10)
                y = random.randint(-(board_size / 2) - 10, (board_size / 2) - 10)

            break
        """

        apple.goto(x, y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        delay -= 0.001
        score += 10

        pen.clear()
        pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Collision for body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

            score = 0
            delay = 0.1

            # Update the score display
            pen.clear()
            pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
            apple.goto(0, board_size / 5)

    time.sleep(delay)

wn.mainloop()
