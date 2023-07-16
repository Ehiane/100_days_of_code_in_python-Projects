#Part 1:
    # create a snake body -- 3 squares(starting length)
    #  motion of the snake -- let the snake move continously forward
    #  motion control -- using keybord events

#Done with part 1

#Part2:
    # put food on the screen
    # detect collision with food and generate food randomly
    # update score
    # end cases detect collision with screen and collision with self(tail).

#Imports:
from turtle import Screen;
from snake import Snake;
import time

# !start of screen
screen = Screen();
screen.setup(width=600, height=600);
screen.bgcolor("black");
screen.title("snake pytonia")

#* turning the tracer off to reduce the frame by frame animation
screen.tracer(0); 

#* Initialising the snake;
snake = Snake();

# !listening for events 
screen.listen();
screen.onkey(fun= snake.up,key="Up");
screen.onkey(fun= snake.down,key="Down");
screen.onkey(fun= snake.left,key="Left");
screen.onkey(fun= snake.right,key="Right");

game_is_on = True;
while game_is_on:
    #responsible for the refresh rate and allows the snake to move as one even though the body is divided into diffrent segments
    screen.update();
    time.sleep(0.1);
    snake.move();














# !end of screen
screen.exitonclick();