"""""
1. Write a Car class that has the following properties: registration number, maximum speed, current speed and travelled distance.
Add a class initializer that sets the first two of the properties based on parameter values.
The current speed and travelled distance of a new car must be automatically set to zero.
Write a main program where you create a new car (registration number ABC-123, maximum speed 142 km/h).
Finally, print out all the properties of the new car.
"""

class Car:
    def __init__(self, registration, maxspeed):
        self.registration = registration
        self.maxspeed = maxspeed
        self.currentspeed = 0
        self.distance = 0


vehicle = Car("ABC-123", 142)
print(f"Car's registration number: {vehicle.registration}")
print(f"Car's maximum speed: {vehicle.maxspeed}")
print(f"Car's current speed: {vehicle.currentspeed}")
print(f"Travelled distance : {vehicle.distance}")

""""
2. Extend the program by adding an accerelate method into the new class. The method should receive the change of speed (km/h) as a parameter.
If the change is negative, the car reduces speed. The method must change the value of the speed property of the object.
The speed of the car must stay below the set maximum and cannot be less than zero. 
Extend the main program so that the speed of the car is first increased by +30 km/h, then +70 km/h and finally +50 km/h. 
Then print out the current speed of the car. Finally, use the emergency brake by forcing a -200 km/h change on the speed and then print out the final speed.
The travelled distance does not have to be updated yet.
"""

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





speed = 30
vehicle = Car("ABC-123", 142)
print(f"Car's registration number: {vehicle.registration}")
print(f"Car's maximum speed: {vehicle.maxspeed}")
print(f"Car's current speed: {vehicle.currentspeed}")
print(f"Travelled distance : {vehicle.distance}")
vehicle.accerelate(30)
print(vehicle.currentspeed)
vehicle.accerelate(70)
print(vehicle.currentspeed)
vehicle.accerelate(60)
print(vehicle.currentspeed)
vehicle.accerelate(-200)
print(vehicle.currentspeed)

"""""
3. Again, extend the program by adding a new drive method that receives the number of hours as a parameter. 
The method increases the travelled distance by how much the car has travelled in constant speed in the given time. 
Example: The travelled distance of car object is 2000 km. The current speed is 60 km/h. Method call car.drive(1.5) increases the travelled distance to 2090 km.
"""
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





speed = 30
vehicle = Car("ABC-123", 142)
print(f"Car's registration number: {vehicle.registration}")
print(f"Car's maximum speed: {vehicle.maxspeed}")
print(f"Car's current speed: {vehicle.currentspeed}")
print(f"Travelled distance : {vehicle.distance}")
vehicle.accerelate(30)
print(vehicle.currentspeed)
vehicle.accerelate(70)
print(vehicle.currentspeed)
vehicle.accerelate(50)
print(vehicle.currentspeed)
vehicle.accerelate(-200)
print(vehicle.currentspeed)

vehicle.distance = 2000
vehicle.accerelate(60)
vehicle.drive(1.5)

print(vehicle.distance)

"""""
Now we will program a car race. The travelled distance of a new car is initialized as zero. At the beginning of the main 
program, create a list that consists of 10 car objects created using a loop. The maximum speed of each new car is a random
value between 100 km/h and 200 km/h. The registration numbers are created as follows: "ABC-1", "ABC-2" and so on. Now the race begins.
One per every hour of the race, the following operations are performed:

The speed of each car is changed so that the change in speed is a random value between -10 km/h and +15 km/h. 
This is done using the accerelate method.
Each car is made to drive for one hour. This is done with the drive method.
The race continues until one of the cars has advanced at least 10,000 kilometers.
Finally, the properties of each car are printed out formatted into a clear table.
"""""
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
        return False
def update_accerelate(car_list):
    for i in car_list:
        i.accerelate(random.randint(-10, 15))
        i.drive(1)
car_list = []
for i in range(10):
    car_list.append(Car("ABC-" + str(i+1), random.randint(100,200)))



while True:
    if distance(car_list):
        break
    update_accerelate(car_list)



properties(car_list)
