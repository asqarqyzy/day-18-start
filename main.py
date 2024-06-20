from turtle import Turtle, Screen
from random import choice, randint
timmy = Turtle()
my_screen = Screen()
my_screen.colormode(255)


def rgb():
    r = randint(0,255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b
#1
# for _ in range(4):
#     timmy.forward(100)
#     timmy.left(90)

#2
# for _ in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

#3
#color_list = ['red', 'blue', 'black', 'brown','yellow', 'green', 'purple']
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     timmy.color(choice(color_list))
#     for _ in range(num_sides):
#         timmy.forward(100)
#         timmy.left(angle)
#
# for num_sides in range(3, 11):
#     draw_shape(num_sides)

#4
# timmy.speed(15)
# timmy.width(5)
# for _ in range(100):
#     timmy.forward(randint(1, 50))
#     timmy.pencolor(rgb())
#     timmy.setheading(choice([90, 180, 270, 0]))

#5
timmy.speed(20)
timmy.width(2)
for _ in range(36):
    timmy.circle(100)
    timmy.color(rgb())
    timmy.setheading(_*10)




my_screen.exitonclick()