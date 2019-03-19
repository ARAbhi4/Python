class Vehicle:
    def __init__(self, name ="", manufacturer ="", madein=""):
        self.name = name
        self.manufacturer = manufacturer

        self.madein = madein

    def stop(self):
        print(self.name , "Car is stop!")

    def driveing(self, drive):
        print("Go to",drive)
    def info(self):
        print("Name: ",self.name,"Manufacturer: ", self.manufacturer, "Made in ",self.madein)

class Car(Vehicle):
    def __init__(self, name="", manufacturer="",madein=""):
        super().__init__(name, manufacturer,madein)
    def stop(self):
        print(self.name, "stop")


z =Vehicle()
c =Car()
c.stop()
z.stop()


