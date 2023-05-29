from turtle import Turtle
import turtle
import random

turtle.colormode(255)
color = [(182, 7, 45), (158, 96, 30), (23, 95, 184), (192, 157, 92), (245, 215, 56), (218, 145, 175), (178, 200, 8),
         (67, 154, 94), (126, 44, 122), (73, 56, 50), (97, 49, 45), (70, 142, 93), (126, 159, 201), (226, 170, 187),
         (185, 94, 117), (128, 174, 141), (92, 123, 175), (204, 101, 63), (166, 207, 177), (167, 189, 225),
         (238, 173, 152), (113, 11, 33), (30, 63, 129), (187, 212, 14), (23, 48, 104), (71, 64, 56)]

tim = Turtle()
tim.hideturtle()
tim.speed("fastest")
tim.penup()
tim.setheading(255)
tim.forward(200)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.color(random.choice(color))
    tim.dot(20)
    tim.penup()
    tim.forward(50)
    # tim.dot(20)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

turtle.exitonclick()
