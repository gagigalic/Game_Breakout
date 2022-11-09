from turtle import Turtle

colors = ["blue", "red", "yellow", "green"]

class Bricks(Turtle):

    def __init__(self):
        super().__init__()
        self.all_bricks=[]
        self.hideturtle()

    def create_bricks(self):

        y=50
        for color in colors:
            for row in range(2):
                x=-260
                y +=25

                while x < 300:

                    new_bricks = Turtle("square")
                    new_bricks.penup()
                    new_bricks.shapesize(stretch_wid=1, stretch_len=3)
                    new_bricks.color(color)
                    new_bricks.goto(x, y)
                    self.all_bricks.append(new_bricks)
                    x +=65

