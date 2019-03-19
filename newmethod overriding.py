class Vehicle:
    """Base class for all vehicles"""

    def __init__(self, name, manufacturer, color):
        print("Creating a Vehicle")
        self.name = name
        self.manufacturer = manufacturer
        self.color = color

class Car(Vehicle):
    """Car class"""

    def __init__(self, name, maufacturer, color, year):
        print("Creating a car")
        super().__init__(name, maufacturer, color)
        self.year = 2017
        self.wheels = 4


if __name__ == "__main__":
    c = Car("Mustang 5.0 GT Coupe", "Ford", "Red", 2017)
    print(c.name, c.year, c.wheels)
