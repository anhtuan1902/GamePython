from random import randint
import turtle


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.point1.x < self.x < rectangle.point2.x and rectangle.point1.y < self.y < rectangle.point2.y:
            return True
        else:
            return False


class Rectangle:

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return (self.point2.x - self.point1.x) * (self.point2.y - self.point1.y)


class GuiRectangle(Rectangle):
    def draw(self, canvas):
        canvas.penup()
        canvas.goto(x=self.point1.x, y=self.point1.y)
        canvas.pencolor('red')
        canvas.pensize(5)

        canvas.pendown()
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)


class GuiPoint(Point):
    def draw(self, canvas, size=5, color='blue'):
        canvas.penup()
        canvas.goto(x=self.x, y=self.y)
        canvas.pendown()
        canvas.dot(size, color)


# Create rectangle object
rectangle = GuiRectangle(Point(x=randint(0, 40), y=randint(0, 40)), Point(x=randint(40, 80), y=randint(40, 80)))

print(f"Rectangle Coordinates: {rectangle.point1.x}, {rectangle.point1.y} and {rectangle.point2.x}, {rectangle.point2.y}")

user_point = GuiPoint(float(input("Guess x: ")), float(input('Guess y: ')))
user_area = float(input('Guess Rectangle area: '))

print("Your point was inside rectangle: ", user_point.falls_in_rectangle(rectangle))
print('Your area was off by: ', rectangle.area() - user_area)

myturtle = turtle.Turtle('turtle')
rectangle.draw(canvas=myturtle)
user_point.draw(canvas=myturtle)
turtle.done()

