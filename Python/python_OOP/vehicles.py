class Vehicle:
    def __init__(self, wheels, capacity, make, model):
        self.wheels = wheels
        self.capacity = capacity
        self.make = make
        self.model = model
        self.mileage = 0

    def reverse(self, miles):
        self.mileage -= miles
        return self

    def drive(self, miles):
        self.mileage += miles
        return self

class Bike(Vehicle):
    def vehicle_type(self):
        return "Bike"

class Car(Vehicle):
    def set_wheels(self):
        self.wheels = 4
        return self

class Airplane(Vehicle):
    def fly(self, miles):
        self.mileage += miles
        return self
