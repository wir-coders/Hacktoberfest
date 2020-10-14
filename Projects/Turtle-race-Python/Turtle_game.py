#!/usr/bin/env python
# This is turtle game using python turtle library

import turtle
from turtle import *
from random import randint

#window
window = turtle.Screen()
window.title("Turtle Race game ")
turtle.bgcolor("cyan")
turtle.speed()
turtle.penup()
turtle.setpos(-200,180)
turtle.write("TURTLE RACE GAME",font=("Arial",30,"bold"))
turtle.pendown()


#turtle 
speed(10)
penup()
goto(-140,120)
for steps in range(15):
  write(steps,align="center")
  right(90)
  forward(10)
  pendown()
  forward(150)
  penup()
  backward(160)
  left(90)
  forward(20)
  
forward(20)

#turtle ada
ada = Turtle()
ada.color('red')
ada.shape('turtle')
ada.penup()
ada.goto(-160,100)
ada.pendown()

#turtle bob
bob = Turtle()
bob.color('green')
bob.shape('turtle')
bob.penup()
bob.goto(-160,70)
bob.pendown()

#turtle jack
jack = Turtle()
jack.color('yellow')
jack.shape('turtle')
jack.penup()
jack.goto(-160,40)
jack.pendown()

#turtle joe
Joe = Turtle()
Joe.color('blue')
Joe.shape('turtle')
Joe.penup()
Joe.goto(-160,10)
Joe.pendown()

#turtle kim
kim =Turtle()
kim.color('black')
kim.shape('turtle')
kim.penup()
kim.goto(-160,-20)
kim.pendown()

#turtle run
for turn in range(100):
    ada.forward(randint(1,5))
    bob.forward(randint(1,5))
    jack.forward(randint(1,5))
    Joe.forward(randint(1,5))
    kim.forward(randint(1,5))

  
  

 



