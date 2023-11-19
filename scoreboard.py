from turtle import Turtle
ALIGNMENT="center"
FONT = ('Black Ops One', 12)
with open("data.text",mode="r") as file:
    phigh_score = int(file.read())

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score=phigh_score
        self.penup()
        self.goto(0,280)
        self.color("red")
        self.hideturtle()
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"score: {self.score}" f" high score:{self.high_score}", align=ALIGNMENT,font = FONT)


    def increase_score(self):
        self.score +=1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.text",mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    #def over(self):
       # self.goto(0,0)
       # self.write("game over",font=('arial',20,'bold'))