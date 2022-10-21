"""""
1. Implement the following class hierarchy using Python: A publication can be either a book or a magazine.
Each publication has a name. Each book also has an author and a page count, whereas each magazine has a chief editor.
Also write the required initializers to both classes. Create a print_information method to both subclasses for printing
out all information of the publication in question. In the main program, create publications Donald Duck
(chief editor Aki Hyyppä) and Compartment No. 6 (author Rosa Liksom, 192 pages). Print out all information of
both publications using the methods you implemented.
"""
class Publication:
    def __init__(self, name):
        self.name = name

class Magazine(Publication):
    def __init__(self, name, editor ):
        self.editor = editor
        super().__init__(name)
    def print_information(self):
        print(self.name, self.editor)

class Book(Publication):
    def __init__(self, name, author, p_count):
        self.author = author
        self.p_count = p_count
        super().__init__(name)
    def print_information(self):
        print(self.name, self.author, str(self.p_count) + " Pages")


magazine = Magazine("Donald Duck", "Aki Hyyppä")
book = Book("Compartment No. 6", "Rosa Liksom", 192 )
magazine.print_information()
book.print_information()

"""""
2. Extend the previosly written Car class by adding two subclasses: ElectricCar and GasolineCar.
Electric cars have the capacity of the battery in kilowatt-hours as their property.
Gasoline cars have the volume of the tank in liters as their property. Write initializers for the subclasses.
For example, the initializer of electric cars receives the registration number, maximum speed and battery capacity as its parameter. 
It calls the initializer of the base class to set the first two properties and then sets its capacity. 
Write a main program where you create one electric car (ABC-15, 180 km/h, 52.5 kWh) and one gasoline car (ACD-123, 165 km/h, 32.3 l). 
Select speeds for both cars, make them drive for three hours and print out the values of their kilometer counters.
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

class ElectricCar(Car):
    def __init__(self, registration, maxspeed, b_capacity):
        self.b_capacity = b_capacity
        super().__init__(registration, maxspeed)
    def print_out(self):
        print(self.registration, self.maxspeed, "km/h", self.b_capacity, "Kwh", self.distance, " km")
class GasolineCar(Car):
    def __init__(self, registration, maxspeed, l_capacity):
        self.l_capacity = l_capacity
        super().__init__(registration, maxspeed)
    def print_out(self):
        print(self.registration, self.maxspeed, "km/h", self.l_capacity, "liters", self.distance, " km")



eve = ElectricCar("ABC-15", 180, 52.5)
gascar = GasolineCar("ABC-123",165, 32.3)
eve.accerelate(100)
gascar.accerelate(100)
eve.drive(3)
gascar.drive(3)
eve.print_out()
gascar.print_out()