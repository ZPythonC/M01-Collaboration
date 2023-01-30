class vehicle(object):
    def __init__(self):
        self.type = input("Please enter your vehicle type: ")
class automobile(vehicle):
    def __init__(self):
        vehicle.__init__(self)
        self.year = input("What year was your " + self.type + " made? ")
        self.make = input("What make is your " + self.type + "? ")
        self.model = input("What model is your " + self.type + "? ")
        self.doors = input("Does your " + self.type + "have 2 or 4 doors? ")
        self.roof = input("Is your " + self.type + "'s roof solid or sun? ")
        self.publish()
    def publish(self):
        print("Vehicle type: " + self.type)
        print("Year: " + self.year)
        print("Make: " + self.make)
        print("Model: " + self.model)
        print("Doors: " + self.doors)
        print("Roof: " + self.roof)
def main():
    automobile()
main()