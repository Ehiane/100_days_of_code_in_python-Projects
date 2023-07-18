#game components:
    # create Screen ##Done
    # create and move paddle ##Done
    # create another paddle ##Done
    # create ball ##Done
    # make the ball move
    # detect collision with wall and bounce
    # detect collision with paddle
    # detect when paddle misses
    # keep score

# %Globals
LEFT_PADDLE_START_POSITION = (-390,0); #i would like for both to be symmetrical but Tkinter is acting up
RIGHT_PADDLE_START_POSITION = (380,0);
ON,OFF= True, False;

# *Imports:
from turtle import Screen;
from paddle import Paddle;
from ball import Ball;

# ! start of screen and set-up
screen = Screen();
screen.tracer(0); #turns off animation.
screen.setup(width=800, height= 800);
screen.bgcolor("black");
screen.title("Pin-Pong");


# @Object Instantiation:
# Paddles
left_paddle = Paddle(LEFT_PADDLE_START_POSITION);
right_paddle = Paddle(RIGHT_PADDLE_START_POSITION);

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

game_engine = ON;

while game_engine:
    # refresh rate
    screen.update(); #updates the screen per frame.





# ! end of screen
screen.exitonclick();