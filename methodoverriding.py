class Vehicle:
    """Base class for all vehicles"""

    def __init__(self, name, manufacture, color):
        self.name = name
        self.manufacture = manufacture
        self.color = color

    def turn(self, direction):
        print("Turning", self.name, "to", direction)

class Car(Vehicle):
    """Car class"""

    def __init__(self, name, manufacturer, color, year):
        self.name = name
        self.manufacture = manufacturer
        self.color = color
        self.year = 2017
        self.wheels = 4

    def change_gear(self, gear_name):
        """Method of changing gear"""
        print(self.name, "is changing gear to", gear_name)

    def turn(self, direction):
        print(self.name, "is turning", direction)

if __name__ == "__main__":
    c = Car("Mustang 5.0 GT Coupe", "Ford", "Red", 2017)
    v = Vehicle("Softail Delux", "Harly-Davidson", "Blue")
    c.turn("right")
    v.turn("right")
