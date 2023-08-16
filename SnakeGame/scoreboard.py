
from turtle import Turtle


class ScoreBoard(Turtle):
  # create board score
  def __init__(self):
    super().__init__()
    self.score = 0
    self.color("white")
    self.penup()
    self.goto(0, 270)
    self.update_scoreboard()
    self.hideturtle()

  # update write score new
  def update_scoreboard(self):
    self.write(f"Score: {self.score}",
               align="center",
               font=('Aria', 20, 'normal'))

  def game_over(self):
    self.goto(0, 0)
    self.write("Game Over!", align="center", font=('Aria', 24, 'normal'))

  # update score when eat food
  def increase_score(self):
    self.score += 1
    self.clear()
    self.update_scoreboard()
