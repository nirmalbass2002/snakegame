from turtle import Turtle
ALIGNMENT="center"
FONT = ('Black Ops One', 12)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0,280)
        self.color("red")
        self.hideturtle()
        self.update_score()


    def update_score(self):
        self.write(f"score: {self.score}", move=False, align=ALIGNMENT,font = FONT)


    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_score()
    def over(self):
        self.goto(0,0)
        self.write("game over",font=('arial',20,'bold'))