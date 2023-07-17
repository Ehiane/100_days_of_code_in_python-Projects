#Imports:
from turtle import Turtle;
STARTTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MAX_SPEED = 21; #this is the maximum distance between segments before seeing visible separation lines.

UP, DOWN,  LEFT, RIGHT = 90, 270, 180, 0;
class Snake:
    def __init__(self):
        self.segments = [];
        self.create_snake();
        self.head = self.segments[0];
        self.speed = 15;


        # * Creating a Snake body
    def create_snake(self):
        """
        initialises the three starting squares of the snake.
        """
        for position in STARTTING_POSITIONS:
            self.add_segment(position);
    
    def move(self):
        """
        moves the snake in forward by 20 pxls
        """
        # we are moving the snake from the back to avoid missing trails
        # for instance 
        #                   motion: 
        # [3][2][1] --> [3&2][1] --> [2][3&1]-> [2][1][3]
        # [1&2][3] --> [1][2&3] --> [1][3][2] --> [1&3][2] --> [3][2&1]
        # [3][2][1]
        segment_end_index = len(self.segments) -1;
        for seg_num in range(segment_end_index,0,-1): #(start,stop,step)
            # starts from the back.
                # getting hold of second to last seg(with coordinates).
            new_x = self.segments[seg_num - 1].xcor();
            new_y = self.segments[seg_num - 1].ycor();
            self.segments[seg_num].goto(new_x,new_y);
        self.head.fd(self.speed);


    def add_segment(self,position):
        new_segment = Turtle("square");
        new_segment.color("white");
        new_segment.pu(); #to stop drawing the line.
        new_segment.goto(position);
        self.segments.append(new_segment);
    
    def extend(self):
        self.add_segment(self.segments[-1].position());
    

    # Directions
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP);

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN);

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT);

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT);

    def move_faster(self):
        if self.speed < MAX_SPEED:
            self.speed += 0.5;
        else:
            print("You have reached max speed")
