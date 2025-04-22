import turtle
turtle.Screen().bgcolor("purple")
turtle.Screen().setup(600,700)
max =turtle.Turtle()
num_sides =4
side_lenght = 200
angle = 360.0 / num_sides
for i in range (num_sides):
    max.forward(side_lenght)
    max.color("black")
    max.right(angle)
turtle.done()