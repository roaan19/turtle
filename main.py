import turtle
turtle.Screen().bgcolor("blue")
turtle.Screen().setup(190,100)

polygon=turtle.Turtle()
sides=6
sidelenght=70
angle=360/sides

for i in range (sides):
    polygon.forward(sidelenght)
    polygon.right(angle)

turtle.done()