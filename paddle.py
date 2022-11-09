from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self, position):
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=6)
        self.color("#EFEFEF")
        self.setpos(position)


    def left(self):
        new_x=self.xcor()-20
        self.goto(new_x, self.ycor())

    def right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

