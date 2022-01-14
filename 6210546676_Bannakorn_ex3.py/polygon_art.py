import turtle
import random

turtle.speed(5)

clr = 'blue'

def polygon(clr):
    while True:
        turtle.penup()
        turtle.color(clr)
        turtle.fillcolor(clr)
        x = random.randint(-400,400)
        y = random.randint(-400,400)
        n = random.randint(3, 9)
        turtle.goto(x, y)
        turtle.pendown()
        turtle.begin_fill()   
        size = random.randint(-100,100)    
        for i in range (n):
            turtle.forward(size)
            turtle.left(360/n)
        turtle.end_fill()
    
          
# while True:

#     x = random.randint(0,100)
#     y = random.randint(0,100)
#     size = random.randint(100,100)
#     n = random.randint(3, 9)



polygon(clr)
