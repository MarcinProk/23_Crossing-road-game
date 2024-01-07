from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.goto(-250, 270)
        self.score = 0
        self.write(f"LEVEL: {self.score}", align= 'left', 
                   font=('Arial', 15, 'normal') )
        self.hideturtle()
        

    def count(self):
        self.score += 1
        self.clear()
        self.write(f"LEVEL: {self.score}", align= 'left', 
                   font=('Arial', 15, 'normal') )
        
    def game_over(self):
        self.color('red')
        self.penup()
        self.goto(0,0)
        self.write(f"GAME OVER", align= 'center', 
                   font=('Arial', 25, 'bold') )
