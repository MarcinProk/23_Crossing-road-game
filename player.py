from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVING_SPEED = 10
FINISH_POSITION = (0, 280)

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.goto(STARTING_POSITION)
        self.seth(90)
    
    def move_up(self):
        self.forward(MOVING_SPEED)

    def move_down(self):
        self.backward(MOVING_SPEED)