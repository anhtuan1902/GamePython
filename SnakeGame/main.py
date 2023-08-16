from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

if __name__ == '__main__':
  screen = Screen()
  screen.setup(width=600, height=600)
  screen.bgcolor("black")
  screen.title("Snake Game")
  screen.tracer(0)

  snake = Snake()
  food = Food()
  scoreboard = ScoreBoard()

  # get control of user
  screen.listen()
  screen.onkey(snake.up, 'Up')
  screen.onkey(snake.down, 'Down')
  screen.onkey(snake.left, 'Left')
  screen.onkey(snake.right, 'Right')

  starting = True
  while starting:

    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
      scoreboard.increase_score()
      snake.extend()
      food.refesh()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor(
    ) > 280 or snake.head.ycor() < -280:
      scoreboard.game_over()
      starting = False

    # detect collision with tail
    for segment in snake.segments[1:]:
      if snake.head.distance(segment) < 10:
        scoreboard.game_over()
        starting = False

  screen.exitonclick()