class Bike:
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print("Price:", self.price, ", Max Speed:",
              self.max_speed, ", Miles:", self.miles)

    def reverse(self):
        print("Reversing")
        self.miles -= 5
        return self
    #in the future, this method could instead simply add miles, we could track reversed miles separately
    #or we could add a check when reducing miles in order to prevent negative miles
    
    def ride(self):
        print("Riding")
        self.miles += 10
        return self
    #ride and reverse can return self to allow for chaining methods
    


bike1 = Bike(200, "25mph")
bike2 = Bike(450, "30mph")
bike3 = Bike(1000, "35mph")

bike1.ride().ride().ride().displayInfo()
bike2.ride().ride().reverse().reverse().displayInfo()
bike3.reverse().reverse().reverse().displayInfo()
