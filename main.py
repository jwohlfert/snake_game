from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

snake_list = []
for i in range(3):
    turtle = Turtle()
    turtle.color("white")
    turtle.shape("square")
    turtle.setx(i * -20)
    snake_list.append(turtle)





screen.exitonclick()
