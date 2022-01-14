import turtle
import random


turtle.speed(10)
turtle.setheading(0)
clr_list = ["red", "blue", "gold", "brown", "violet", "pink", "orange", "yellow"]


def pinwheel(num_branch,size,backup):
    turtle.penup()
    random_clr = random.randint(0, 7)
    turtle.color(clr_list[random_clr])
    turtle.fillcolor(clr_list[random_clr])

    random_size = random.randint(0, 30)
    turtle.pensize(random_size)
    ran_x = random.randint(-400, 400)
    ran_y = random.randint(-400, 400)
    turtle.goto(ran_x, ran_y)
    turtle.pendown()
    turtle.begin_fill()

    for c in range(num_branch):
        turtle.forward(size)
        turtle.backward(backup)
        turtle.left(360/num_branch)



for c in range(0, 9):
    num_branch = random.randint(3, 10)
    size = random.randint(30, 250)
    backup = random.randint(30, 250)
    pinwheel(num_branch, size, backup)
turtle.done()
