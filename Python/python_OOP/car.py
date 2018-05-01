class Car:
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.mileage = mileage
        self.fuel = fuel
        self.tax = 0.12
        if price > 10000:
            self.tax = 0.15
        self.displayAll()

    def displayAll(self):
        print("Price:", self.price, "\nSpeed:",
              self.speed, "\nFuel:", self.fuel, "\nMileage:", self.mileage, "\nTax: ", self.tax)


car1 = Car(5000, "55mph", "Empty", "12mpg")
car2 = Car(35000, "75mph", "Full", "28mpg")
car3 = Car(25000, "65mph", "Half Full", "25mpg")
car4 = Car(2000, "45mph", "Almost Empty", "8mpg")
car5 = Car(115000, "105mph", "Full", "30mpg")
car6 = Car(45000, "85mph", "Empty", "32mpg")

