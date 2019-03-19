import turtle

class AjobTurtle(turtle.Turtle):
    """AjobTurtle is a class for new type of turtle"""
    def forward(self, distance):
        super().backward(distance)


    def back(self, distance):
        super().forward(distance)

    def left(self, angle):
        super().right(angle)

    def right(self, angle):
        super().left(angle)

if __name__ == "__main__":
    montu = AjobTurtle()
    montu.left(30)
    montu.forward(200)
    montu.left(45)
    montu.back(100)
    montu.right(90)
    montu.forward(10)

    jhontu = turtle.Turtle()
    jhontu.shape("turtle")
    jhontu.left(30)
    jhontu.forward(200)
    jhontu.left(45)
    jhontu.back(100)
    jhontu.right(90)
    jhontu.forward(10)

    turtle.done()
