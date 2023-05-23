from turtle import Turtle, Screen

mitch = Turtle()
scr = Screen()

mitch.speed(10)

def move_forwards():
    mitch.forward(10)

def move_back():
    mitch.back(10)

def rotate_left():
    mitch.left(10)

def rotate_right():
    mitch.right(10)

def erase():
    mitch.reset()

scr.listen()
scr.onkey(key="w", fun=move_forwards)
scr.onkey(key="s", fun=move_back)
scr.onkey(key="a", fun=rotate_left)
scr.onkey(key="d", fun=rotate_right)
scr.onkey(key="c", fun=erase)

scr.exitonclick()

