# [p]oop uses the class as a blueprint
# and the object as what's called an 'instance'

# Rectangle is a class
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


r1 = Rectangle(5, 3) # r1 is an object
print("Area:", r1.area())
