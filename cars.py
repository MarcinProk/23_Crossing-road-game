from turtle import Turtle, Screen
import random, time

COLORS = ['red', 'orange', 'blue', 'yellow', 'silver', 'purple', 'green']
STARTING_MOVE_SPEED = 5
SPEED_INCREASE = 10
screen = Screen()
screen.addshape(R"C:\Users\marci\Desktop\Programowanie\KURSY\100_exercise\exercises\days 21-30\day23_crossing\car_picture.gif")

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_SPEED

    def generate_cars(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape(R"C:\Users\marci\Desktop\Programowanie\KURSY\100_exercise\exercises\days 21-30\day23_crossing\car_picture.gif")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(290, random_y)
            self.all_cars.append(new_car)
        
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def speed_up(self):
        self.car_speed += SPEED_INCREASE