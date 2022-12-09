from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake_list = []
for i in range(3):
    turtle = Turtle()
    turtle.color("white")
    turtle.shape("square")
    turtle.penup()
    turtle.setx(i * -20)
    snake_list.append(turtle)
screen.update()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(snake_list) - 1, 0, -1):
        new_x = snake_list[seg_num - 1].xcor()
        new_y = snake_list[seg_num - 1].ycor()
        snake_list[seg_num].goto(x=new_x, y=new_y)
    snake_list[0].forward(20)



screen.exitonclick()
