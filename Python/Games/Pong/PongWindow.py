# By @rsoemardja
# Part 1: Getting Started

#Drawing pixel Lines with Python with the turtle library
import turtle
#import os it allows us to interact with the Operation System based on text commands
import os
#winsound is Exclusive to windows
import winsound

wn = turtle.Screen()
wn.title("Pong by @rsoemardja")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Score
score_a = 0
score_b = 0

# Paddle A
"""This is known as a turtle object for paddle_a"""
paddle_a = turtle.Turtle()
"""this is the speed of the Paddle"""
paddle_a.speed(0)
"""This is the shape of the Paddle"""
paddle_a.shape("square")
"""This is to create size for the shape of the Paddle"""
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
"""This is the color of the Paddle"""
paddle_a.color("white")
paddle_a.penup()
"""it is saying where the Paddle go's to in the x and y axis"""
paddle_a.goto(-350, 0)


# Paddle B
"""This is known as a turtle object for paddle_b"""
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0)


# Ball
ball = turtle.Turtle()
ball.speed(-6)
ball.shape("square")
"""since it is the ball it requires no increased size"""
ball.color("white")
ball.penup()
"""The ball will go to the center"""
ball.goto(0, 0)
# Ball Movement
"""It is going to move to the right by 2 pixels"""
ball.dx = 2
"""It is going to move to the up direction by 2 pixels"""
ball.dy = -2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A:0 Player B:0", align="center", font=("Courier", 24,"normal"))


# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard binding
wn.listen()
"""This moves the paddle a with the w and s key"""
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
"""This moves the paddle b with the up and down key"""
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop:
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    
    #Top and Bottom
    """Y axis"""
    if ball.ycor() > 290:
       ball.sety(290)
       ball.dy *= -1
       winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
       """aplay is for linux"""
       """afplay is for mac"""

    elif ball.ycor() < -290:
       ball.sety(-290)
       ball.dy *= -1
       winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    #Left and right
    """X axis"""
    if ball.xcor() > 350:
    #"""It will go set to the center"""
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -350:
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    #Paddle and Ball collisions
    if (ball.xcor() < -340 and ball.ycor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -50):
       """ball/setx(340)"""
       ball.dx *= -1
       winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    elif (ball.xcor() > 340 and ball.ycor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -50):
       ball.dx *= -1
       winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
