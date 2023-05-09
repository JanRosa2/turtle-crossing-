from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.goto(-280, 260)
        self.level = 0
        self.write(arg=f"Level: {self.level}", align="left", font=("Ariel", 20, "normal"))

    def next_level(self):
        self.level += 1
        self.clear()
        self.write(arg=f"Level: {self.level}", align="left", font=("Ariel", 20, "normal"))

    def new_game(self):
        self.level += 0
        self.clear()
        self.write(arg=f"Level: {self.level}", align="left", font=("Ariel", 20, "normal"))

    def end_game(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=("Ariel", 20, "normal"))

