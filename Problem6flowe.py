#Cecilia Zacarias
#2/27/2020

#Problem #6 this program uses a polygon program to coverted to a function to create a pattern.

import turtle
ceci = turtle.Turtle()

sides = int(input ("Number of sides in polygon?"))
length = int (input ("What length would you like the sides?"))

ceci = turtle.Turtle()

#ceci.color(str(lcolor))
#ceci.pencolor(str(lcolor))

def drawPolygon(t,sides,length):
    
    for i in range(sides):
    #ceci.pencolor = (str(lcolor))
    #ceci.fillcolor = (str(fcolor))
        ceci.forward(length)
        ceci.left(360 / sides)

wn = turtle.Screen()
ceci = turtle.Turtle()
ceci.speed(5)
ceci.pencolor("blue")
mv = -10

for s in range(length, 10*length,40):
   
  drawPolygon(ceci,sides,s)

  ceci.penup()
  ceci.goto(mv,mv)
  ceci.pendown()
  mv = mv -10



