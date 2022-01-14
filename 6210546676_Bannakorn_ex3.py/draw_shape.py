import turtle
import random

# Set to slowest speed and east heading.
# To increase the speed, use the following guide:
# “fast”: 10 “normal”: 6 “slow”: 3 “slowest”: 1

turtle.speed(3)
turtle.setheading(0)

while True:
    # draw square
    turtle.penup()
    turtle.color("blue")
    turtle.fillcolor("blue")
    x = random.randint(0,100)
    y = random.randint(0,100)
    turtle.goto(x,y)
    turtle.pendown()
    turtle.begin_fill()
    size = random.randint(-100,100)
    for i in range (4):
        turtle.forward(size)
        turtle.left(90)
    turtle.end_fill()

    # draw triangle
    turtle.penup()
    turtle.color("blue")
    turtle.fillcolor("blue")
    x = random.randint(0,100)
    y = random.randint(0,100)
    turtle.goto(x,y)
    turtle.pendown()
    turtle.begin_fill()
    size = random.randint(-100,100)
    for i in range (3):
        turtle.forward(size)
        turtle.left(120)
    turtle.end_fill()

    # draw pentagon
    turtle.penup()
    turtle.color("blue")
    turtle.fillcolor("blue")
    x = random.randint(0,100)
    y = random.randint(0,100)
    turtle.goto(x,y)
    turtle.pendown()
    turtle.begin_fill()
    size = random.randint(-100,100)
    for i in range (5):
        turtle.forward(size)
        turtle.left(72)
    turtle.end_fill()

    # # hold the window; close it by clicking the window close 'x' mark
    # turtle.done()