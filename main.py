from turtle import Turtle,Screen
import random

screen = Screen()
screen.setup(width=600 , height=600)
all_turtle = []
y_position = [-70, 70]
y_circle_position = [-100, 40]
colors = ["blue","green"]
is_race_on = False



for turtle in range(0,2):

    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.hideturtle()
    new_turtle.color(colors[turtle])
    new_turtle.goto(x=260, y= y_circle_position[turtle])
    new_turtle.pendown()
    new_turtle.circle(30)

    new_turtle.penup()
    new_turtle.showturtle()
    new_turtle.goto(x=-280 ,y= y_position[turtle])
    all_turtle.append(new_turtle)


is_race_on = True

while is_race_on:

    for turtle2 in all_turtle:
        winning_color = turtle2.pencolor()
        if turtle2.xcor() > 250:
            is_race_on = False
            print(f"The winer is {winning_color}")

        random_distance = random.randint(0, 10)
        turtle2.forward(random_distance)











screen = Screen()
screen.exitonclick()
