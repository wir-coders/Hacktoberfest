'''Created by Aakasha01Agarwal'''


import turtle

t=turtle.Turtle()

def init():

    t.getscreen().bgcolor('black')
    t.color('white')
    t.speed(1)                    #Change the speed here
    t.setheading(90)


def branch(l, angle):
    if l > 10:
        t.forward(l)
        t.right(angle)
        branch(l-15, angle)
        t.left(2*angle)
        branch(l-15, angle)
        t.right(angle)
        t.back(l)

init()
branch(100, 30)   ##takes length and angle in that order

turtle.done()