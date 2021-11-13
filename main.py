# Code written by - Amish Verma
# Original date of writing - 11/11/2021
# Project Title - Snake Game
# GitHub - www.github.com/thisisamish
# Twitter - www.twitter.com/thisisamish
# This project was created as a part of the #100DaysOfCode challenge I undertook
# as a part of "The Complete Python Pro Bootcamp for 2022" course by Angela Yu on Udemy.
# Please report any bugs you find; and if you want, then try to make the code more efficient. Thank you!

from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Classic Nokia Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect Collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
