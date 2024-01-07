from turtle import Screen
import time
from player import Player
from cars import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move_up, 'Up')
screen.onkey(player.move_down, 'Down')


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.generate_cars()
    car_manager.move_cars()

    if player.ycor() > 290:
        scoreboard.count()
        car_manager.speed_up()
        player.goto(0,-280)

    for car in car_manager.all_cars:
        if player.distance(car) <= 20:
            game_is_on = False
            scoreboard.game_over()

screen.mainloop()
