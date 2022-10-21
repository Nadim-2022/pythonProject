"""""
1. Write an Elevator class that receives the numbers of the bottom and top floors as initializer parameters.
The elevator has methods go_to_floor, floor_up and floor_down. A new elevator is always at the bottom floor.
If you make elevator h for example the method call h.go_to_floor(5), the method calls either the floor_up or 
floor_down methods as many times as it needs to get to the fifth floor. The methods run the elevator one floor up or
down and tell what floor the elevator is after each move. Test the class by creating an elevator in the main program, 
tell it to move to a floor of your choice and then back to the bottom floor.
"""""
class Elevator:
    def __init__(self):
        self.floor = 0
    def floor_up(self):
        self.floor += 1
    def floor_down(self):
        self.floor -= 1
    def go_to_floor(self,num):
        while True:
            if self.floor > num:
                self.floor_down()
                print(self.floor)
            elif self.floor < num:
                print(self.floor)
                self.floor_up()
            else:
                break


h = Elevator()
h.go_to_floor(5)

h.go_to_floor(2)

"""""
2. Extend the previous program by creating a Building class. The initializer parameters for the class are the numbers of
the bottom and top floors and the number of elevators in the building. When a building is created, the building creates 
the required number of elevators. The list of elevators is stored as a property of the building. Write a method called 
run_elevator that accepts the number of the elevator and the destination floor as its parameters. In the main program, 
write the statements for creating a new building and running the elevators of the building.
"""
class Elevator:
    def __init__(self):
        self.floor = 0
    def floor_up(self):
        self.floor += 1
    def floor_down(self):
        self.floor -= 1
    def go_to_floor(self,num):
        while True:
            if self.floor > num:
                self.floor_down()
                print(self.floor)
            elif self.floor < num:
                print(self.floor)
                self.floor_up()
            else:
                break


class Building:
    def __init__(self, num):
        self.elevators = []
        for i in range(num):
            self.elevators.append(Elevator())

    def run_elevator(self, ele_num, floor):
        self.elevators[ele_num].go_to_floor(floor)

b = Building(5)

b.run_elevator(3, 6)

print(b.elevators[3].floor)


"""""
3. Extend the program again by adding a method fire_alarm that does not receive any parameters and 
moves all elevators to the bottom floor. Continue the main program by causing a fire alarm in your building.
"""
class Elevator:
    def __init__(self):
        self.floor = 0
    def floor_up(self):
        self.floor += 1
    def floor_down(self):
        self.floor -= 1
    def go_to_floor(self,num):
        while True:
            if self.floor > num:
                self.floor_down()
                print(self.floor)
            elif self.floor < num:
                print(self.floor)
                self.floor_up()
            else:
                break


class Building:
    def __init__(self, num):
        self.elevators = []
        for i in range(num):
            self.elevators.append(Elevator())

    def run_elevator(self, ele_num, floor):
        self.elevators[ele_num].go_to_floor(floor)
    def fire_alarm(self):
        for i in self.elevators:
            i.go_to_floor(0)

b = Building(5)

b.run_elevator(3, 6)

print(b.elevators[3].floor)

b.fire_alarm()

"""""
4. This exercise continues the previous car race exercise from the last exercise set. Write a Race class that has the following properties: 
name, distance in kilometers and a list of cars participating in the race. The class has an initializer that receives the name, kilometers,
and car list as parameters and sets their values to the corresponding properties in the class. The class has the following methods:

hour_passes, which performs the operations done once per hour in the original exercise: generates a random change of speed for each car and calls their drive method.
print_status, which prints out the current information of each car as a clear, formatted table.
race_finished, which returns True if any of the cars has reached the finish line, meaning that they have driven the entire distance of the race.

Write a main program that creates an 8000-kilometer race called Grand Demolition Derby. The new race is given a list of 
ten cars similarly to the earlier exercise. The main program simulates the progressing of the race by calling the hour_passes in a loop,
after which it uses the race_finished method to check if the race has finished. The current status is printed out using the print_status
method every ten hours and then once more at the end of the race.
"""
import random
class Car:

    def __init__(self, registration, maxspeed):
        self.registration = registration
        self.maxspeed = maxspeed
        self.currentspeed = 0
        self.distance = 0
    def accerelate(self, addspeed):
        accelaretion = self.currentspeed + addspeed
        if self.maxspeed > accelaretion:
            self.currentspeed+=addspeed
            if  accelaretion < 0:
                self.currentspeed = 0
    def drive(self, hours):
        self.distance = self.distance + self.currentspeed*hours


def properties(car_list):
    for i in car_list:
        print(i.registration, i.maxspeed, i.currentspeed, i.distance)
def distance(car_list):
    for i in car_list:
        if i.distance > 10000:
            return True

def update_accerelate(car_list):
    for i in car_list:
        i.accerelate(random.randint(-10, 15))
        i.drive(1)

class Race:
    def __init__(self, name, d_km, car_list):
        self.name = name
        self.d_km = d_km
        self.car_list = car_list
    def hour_passes(self):
        update_accerelate(self.car_list)
        for i in self.car_list:
            i.drive(1)
    def race_finished(self):
        for i in self.car_list:
            if i.distance < self.d_km:
                return False
    def __repr__(self):
        text = "Speed (km/h) | Distance (km)`\n"
        for i in self.car_list:
            text+= str(i.currentspeed)+ "km/h | "+ str(i.distance)+ "km\n"
        return text
    def print_status(self):
        for i in car_list:
            i.drive(10)
            print(i.registration, i.maxspeed, i.currentspeed, i.distance)


car_list = []
for i in range(10):
    car_list.append(Car("ABC-" + str(i+1), random.randint(100,200)))
r = Race("Grand Demolition Derby", 8000,car_list)
for i in range(8000):
    print(i)
    if r.race_finished():
        break
    r.hour_passes()

r.print_status()

