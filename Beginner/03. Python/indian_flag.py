import turtle
turtle.penup()
turtle.goto(-100,100)
turtle.color("black")


#orange

turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("#FF9933")
turtle.left(90)
turtle.forward(90)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(90)
turtle.right(90)
turtle.forward(600)
turtle.end_fill()

#white and Ashoka Chakra

turtle.left(90)
turtle.forward(90)
turtle.left(90)
turtle.forward(300)
#turtle.begin_fill()
#turtle.fillcolor("blue")
turtle.circle(45)

#Here is Ashok Chakra with spokes centre of the circle would be at 200,55
turtle.penup()
turtle.goto(200,55)
turtle.color("blue")
for spoke in range(0,24):
  turtle.goto(200,55)
  turtle.right(15)
  turtle.pendown()
  turtle.forward(45)
  turtle.penup()

#turtle.end_fill()
turtle.goto(200,10)
turtle.pendown()
turtle.color("black")
turtle.forward(300)
turtle.left(90)
turtle.forward(90)



#come back to the start of line 3

turtle.penup()
turtle.goto(-100,10)
turtle.right(180)

#green

turtle.begin_fill()
turtle.fillcolor("#138808")
turtle.pendown()
turtle.forward(90)
turtle.left(90)
turtle.forward(600)
turtle.left(90)
turtle.forward(90)
turtle.end_fill()



#come back to line 4

turtle.penup()
turtle.goto(-100,-80)
turtle.right(180)
