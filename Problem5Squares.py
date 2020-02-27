#Cecilia Zacarias
#2/27/2020

#Problem #5 we are going to use a base code that I will identify later on to create a sqaure image
# this the chunk of code that was given that we will use as a base to produce a sqaure image.


import turtle
def drawSquare(t,side):
  
  for i in range(4):
  
      t.forward(side)
      t.left(90)


wn = turtle.Screen()
#wn.bgcolor("light green")
ceci = turtle.Turtle()
#ceci.fillcolor("blue")
ceci.speed(5)
ceci.pencolor("blue")
mv = -10


for s in range(20, 101,20):
   
  drawSquare(ceci,s)

  ceci.penup()
  ceci.goto(mv,mv)
  ceci.pendown()
  mv = mv -10
  


wn.exitonclick()
