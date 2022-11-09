import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from bricks import Bricks
from scoreboard import Scoreboard

screen = Screen()
screen.title("Game Breakout")
screen.setup(width=600, height=800)
screen.bgcolor("#5A8F7B")
screen.tracer(0)


scoreboard = Scoreboard()
paddle= Paddle((0, -300))
ball = Ball()
bricks = Bricks()
bricks.create_bricks()

screen.listen()
screen.onkey(paddle.left, "Left")
screen.onkey(paddle.right, "Right")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


    if ball.xcor() > 280 or ball.xcor() < -280:
        ball.bounce_x()

    if ball.distance(paddle) < 30 and ball.ycor() > -300:
        ball.bounce_y()

    if ball.ycor() < -300:
        ball.reset_position()
        scoreboard.update_lives()
        if scoreboard.lives ==0:
            scoreboard.game_is_over()
            game_is_on= False

    for brick in bricks.all_bricks:
        if ball.distance(brick) < 35:
            ball.bounce_y()
            brick.hideturtle()
            bricks.all_bricks.remove(brick)
            scoreboard.point()
















screen.exitonclick()

