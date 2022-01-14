import turtle

# 1

turtle.penup()
turtle.pensize(10)
turtle.color("blue")
turtle.pendown()
turtle.circle(100, 360, 6)

turtle.left(90)
turtle.penup()
turtle.color("red")
turtle.pendown()
turtle.circle(100, 360, 6)

turtle.right(270)
turtle.color("yellow")
turtle.circle(100, 360, 6)

turtle.left(90)
turtle.color("green")
turtle.circle(100, 360, 6)

turtle.done()

# ----------------------------------------------

# 2

turtle.goto(-50,0)
turtle.color("red")
turtle.fillcolor("red")
turtle.pensize(3)
turtle.pendown()
turtle.begin_fill()

# red_up

turtle.forward(90)
turtle.left(90)
turtle.forward(400)
turtle.left(90)
turtle.forward(90)
turtle.left(90)
turtle.forward(400)

# red_down
turtle.forward(400)
turtle.left(90)
turtle.forward(90)
turtle.left(90)
turtle.forward(400)


# red_right
turtle.right(90)
turtle.forward(675)
turtle.left(90)
turtle.forward(90)
turtle.left(90)
turtle.forward(775)

# red_left
turtle.forward(675)
turtle.left(90)
turtle.forward(90)
turtle.left(90)
turtle.forward(775)

turtle.end_fill()
turtle.penup()

# top_left
turtle.penup()
turtle.goto(-200,125)
turtle.pendown()
turtle.color("red")
turtle.fillcolor("red")
turtle.pensize(3)
turtle.begin_fill()
turtle.left(150)
turtle.forward(600)
turtle.left(90)
turtle.forward(55)
turtle.left(90)
turtle.forward(510)
turtle.left(30)
turtle.forward(108)

turtle.end_fill()
turtle.penup()


# top_right
turtle.penup()
turtle.goto(200,125)
turtle.pendown()
turtle.color("red")
turtle.fillcolor("red")
turtle.pensize(3)
turtle.begin_fill()
turtle.right(150)
turtle.forward(-600)
turtle.right(90)
turtle.forward(-55)
turtle.right(90)
turtle.forward(-510)
turtle.right(30)
turtle.forward(-108)

turtle.end_fill()
turtle.penup()


# bottom_left
turtle.penup()
turtle.goto(-200,-45)
turtle.pendown()
turtle.color("red")
turtle.fillcolor("red")
turtle.pensize(3)
turtle.begin_fill()
turtle.right(150)
turtle.forward(600)
turtle.right(90)
turtle.forward(55)
turtle.right(90)
turtle.forward(510)
turtle.right(30)
turtle.forward(108)

turtle.end_fill()
turtle.penup()

# bottom_right
turtle.penup()
turtle.goto(200,-45)
turtle.pendown()
turtle.color("red")
turtle.fillcolor("red")
turtle.pensize(3)
turtle.begin_fill()
turtle.left(150)
turtle.forward(-600)
turtle.left(90)
turtle.forward(-55)
turtle.left(90)
turtle.forward(-510)
turtle.left(30)
turtle.forward(-108)

turtle.end_fill()
turtle.penup()


# top_left_blue
turtle.penup()
turtle.goto(-100,130)
turtle.pendown()
turtle.color("blue")
turtle.fillcolor("blue")
turtle.pensize(3)
turtle.begin_fill()
turtle.left(150)
turtle.forward(600)
turtle.right(150)
turtle.forward(520)
turtle.right(90)


turtle.end_fill()
turtle.penup()

# top_left_b_blue
turtle.penup()
turtle.goto(-400,125)
turtle.pendown()
turtle.color("blue")
turtle.fillcolor("blue")
turtle.pensize(3)
turtle.begin_fill()
turtle.right(120)
turtle.forward(400)
turtle.left(90)
turtle.forward(230)
turtle.left(90)

turtle.end_fill()
turtle.penup()


# top_right_blue
turtle.penup()
turtle.goto(100,130)
turtle.pendown()
turtle.color("blue")
turtle.fillcolor("blue")
turtle.pensize(3)
turtle.begin_fill()
turtle.left(60)
turtle.forward(600)
turtle.left(150)
turtle.forward(520)
turtle.left(90)

turtle.end_fill()
turtle.penup()

# top_right_b_blue
turtle.penup()
turtle.goto(400,125)
turtle.pendown()
turtle.color("blue")
turtle.fillcolor("blue")
turtle.pensize(3)
turtle.begin_fill()
turtle.left(90)
turtle.forward(400)
turtle.left(90)
turtle.forward(230)


turtle.end_fill()
turtle.penup()


# bottom_left_blue
turtle.penup()
turtle.goto(-100,-50)
turtle.pendown()
turtle.color("blue")
turtle.fillcolor("blue")
turtle.pensize(3)
turtle.begin_fill()
turtle.left(-60)
turtle.forward(-680)
turtle.right(30)
turtle.forward(590)
turtle.left(90)

turtle.end_fill()
turtle.penup()

# bottom_left_b_blue
turtle.penup()
turtle.goto(-400,-45)
turtle.pendown()
turtle.color("blue")
turtle.fillcolor("blue")
turtle.pensize(3)
turtle.begin_fill()
turtle.left(90)
turtle.forward(400)
turtle.left(90)
turtle.forward(230)
turtle.left(90)

turtle.end_fill()
turtle.penup()

# bottom_right_blue
turtle.penup()
turtle.goto(100,-50)
turtle.pendown()
turtle.color("blue")
turtle.fillcolor("blue")
turtle.pensize(3)
turtle.begin_fill()
turtle.right(90)
turtle.forward(500)
turtle.left(90)
turtle.forward(680)


turtle.end_fill()
turtle.penup()

# bottom_right_b_blue
turtle.penup()
turtle.goto(400,-45)
turtle.pendown()
turtle.color("blue")
turtle.fillcolor("blue")
turtle.pensize(3)
turtle.begin_fill()
turtle.forward(400)
turtle.right(90)
turtle.forward(230)
# turtle.left(90)

turtle.end_fill()
turtle.penup()

turtle.penup()
turtle.goto(-50,0)
turtle.color("red")
turtle.fillcolor("red")
turtle.pensize(3)
turtle.pendown()
turtle.begin_fill()
turtle.right(180)
turtle.forward(90)
turtle.right(90)
turtle.forward(90)
turtle.right(90)
turtle.forward(90)

turtle.end_fill()
turtle.penup()


turtle.done()

# ----------------------------------

# 3 

turtle.pendown()
turtle.color("yellow")
turtle.fillcolor("yellow")
turtle.pensize(10)
turtle.begin_fill()
turtle.circle(100, 360, 4)
turtle.end_fill()
turtle.penup()


turtle.pendown()
turtle.color("black")
turtle.pensize(1)
turtle.circle(100, 360, 4)
turtle.penup()


turtle.goto(-25,50)
turtle.pendown()
turtle.color("black")
turtle.fillcolor("black")
turtle.pensize(5)
turtle.begin_fill()
turtle.left(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(50)
turtle.end_fill()
turtle.penup()

# greem
turtle.goto(0,80)
turtle.pendown()
turtle.color("green")
turtle.fillcolor("green")
turtle.pensize(3)
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()
turtle.penup()

# yellow
turtle.goto(0,115)
turtle.pendown()
turtle.color("yellow")
turtle.fillcolor("yellow")
turtle.pensize(5)
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()
turtle.penup()

# red
turtle.goto(0,145)
turtle.pendown()
turtle.color("red")
turtle.fillcolor("red")
turtle.pensize(5)
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()
turtle.penup()




turtle.done()

