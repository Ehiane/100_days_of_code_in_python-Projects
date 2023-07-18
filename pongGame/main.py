#game components:
    # create Screen ##Done
    # create and move paddle ##Done
    # create another paddle ##Done
    # create ball ##Done
    # make the ball move ##Done
    # detect collision with wall and bounce ##Done
    # detect collision with paddle ##Done
    # detect when paddle misses
    # keep score

# %Globals
LEFT_PADDLE_START_POSITION = (-350,0); #i would like for both to be symmetrical but Tkinter is acting up
RIGHT_PADDLE_START_POSITION = (350,0);
ON,OFF= True, False;

# *Imports:
from turtle import Screen;
from paddle import Paddle;
from ball import Ball;
import time as t;
from scoreboard import ScoreBoard;

# ! start of screen and set-up
screen = Screen();
screen.tracer(0); #turns off animation.
screen.setup(width=800, height= 800);
screen.bgcolor("black");
screen.title("Pin-Pong");


# @Object Instantiation:
# Paddles
left_paddle = Paddle(LEFT_PADDLE_START_POSITION, name="player1");
right_paddle = Paddle(RIGHT_PADDLE_START_POSITION, name="player2");

# Ball
ball = Ball();

# mapping events to key
screen.listen();


#Left paddle
screen.onkey(fun=left_paddle.up, key="w");
screen.onkey(fun=left_paddle.down, key="s");

#Right paddle
screen.onkey(fun=right_paddle.up, key="Up");
screen.onkey(fun=right_paddle.down, key="Down");

# ScoreBoard
score_board = ScoreBoard();

game_engine = ON;

while game_engine:
    # refresh rate
    t.sleep(ball.trajectory);
    screen.update(); #updates the screen per frame.
    ball.move();

    # Detect collision on top and bottom walls
    if ball.ycor() > 375 or ball.ycor() < -325:
        ball.bounce_y();
        pass;

    #Detect collision with paddles.
    
        # Right collision:
    if ball.distance(right_paddle) < 50 and ball.xcor() > 325:
        ball.bounce_x();
        pass;
    
        # Left collision:
    if ball.distance(left_paddle) < 50 and ball.xcor() < -325:
        ball.bounce_x();
        pass;

    # Detect when the ball goes passed the paddle and into the winners side
    if ball.xcor() > 420 and ball.distance(right_paddle) > 50:
        # +1 score for left_paddle;
        ball.reset();
        score_board.update_left_score();
        

    if ball.xcor() < -420 and ball.distance(right_paddle) > 50:
        # +1 score for right_paddle;
        ball.reset();
        score_board.update_right_score();
        



    





# ! end of screen
screen.exitonclick();