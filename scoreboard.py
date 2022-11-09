from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("#EFEFEF")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.lives = 5
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 350)
        self.write(f"SCORE:{self.score}", align="center", font= ("Arial", 25, "bold"))
        self.goto(200, 350)
        self.write(f"LIVES:{self.lives}", align="center", font =("Arial", 25, "bold"))

    def update_lives(self):
        self.lives -=1
        self.update_scoreboard()

    def point(self):
        self.score +=1
        self.update_scoreboard()

    def game_is_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font= ("Arial", 25, "bold"))