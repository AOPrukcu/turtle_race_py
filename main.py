from turtle import Turtle,Screen
import  random

screen = Screen()
screen.setup(width=500,height=400)
is_race_on = False

user_bet = screen.textinput(title="make your bet",prompt="which turtle will win the race enter a color:")
colors = ["yellow","red","magenta","purple","green","orange"]
y_positons= [-70,-40,-10,10,40,70]
all=[]



for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positons[turtle_index])
    all.append(new_turtle)

if user_bet:
    is_race_on=True

while  is_race_on:

    for turtle in all:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle is the winner")
            else:
                print(f"You lost! The {winning_color} turtle is the winner")

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)






screen.exitonclick()
