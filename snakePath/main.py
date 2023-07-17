#Part 1:
    # create a snake body -- 3 squares(starting length)
    #  motion of the snake -- let the snake move continously forward
    #  motion control -- using keybord events

#& --> Done with part 1

#Part2:
    # put food on the screen
    # detect collision with food and generate food randomly
    # update score
    # end cases detect collision with screen and collision with self(tail).

#Import(s):
from turtle import Screen;
from snake import Snake;
import time
from food import Food;
from scoreboard import ScoreBoard;


restart_key = False;

def key_press():
    global restart_key;
    restart_key = True;



# !start of screen
screen = Screen();
screen.setup(width=600, height=600);
screen.bgcolor("black");
screen.title("snake pytonia")

#* turning the tracer off to reduce the frame by frame animation
screen.tracer(0); 

#* Initialising the snake;
snake = Snake();

#* Initialising the food;
food = Food();

#* Initialising the score board;
score_board = ScoreBoard();

# !listening for events 
screen.listen();
screen.onkey(fun= snake.up,key="Up");
screen.onkey(fun= snake.down,key="Down");
screen.onkey(fun= snake.left,key="Left");
screen.onkey(fun= snake.right,key="Right");

def check_key():
    if restart_key: 
        score_board.clear();
        indicator = screen.textinput(title="Do you want to restart?", prompt="Yes or No").lower();
        if indicator == "yes":
            play_game();


screen.listen();
screen.onkeypress(key_press, 'space');


def play_game():
    game_is_on = True;
    while game_is_on:
        #responsible for the refresh rate and allows the snake to move as one even though the body is divided into diffrent segments
        screen.update();
        time.sleep(0.1);
        snake.move();

        #Detect Collision with food;
        if snake.head.distance(food) <  15: #since the food is 10x10 pixels, we give a room of 5 just for ease. once this occurs then we can say that there is a collision.
            print("score +1");
            food.refresh();
            snake.extend(); 
            score_board.update_score();
            if score_board.score % 10 == 0 and score_board.score > 0: #move faster for every multiple of 10;
                snake.move_faster();

        #Detect collision with wall:
        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            score_board.end_game();
            # check_key();
            game_is_on = False;
    

        #Detect collision with Tail.
        new_segemnts = snake.segments[1:];
        for segment in new_segemnts:
            if snake.head.distance(segment) < 10:
                score_board.end_game();
                game_is_on = False;
        
        # if tail collides with any of thr body segments
        #trigger end game .

screen.onkey(fun= play_game,key="Tab");


# & Screen Prompt.
score_board.clear();
score_board.Write("Hit 'tab' to play");










# !end of screen
screen.exitonclick();