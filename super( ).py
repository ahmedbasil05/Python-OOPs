class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}.")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):    #method overriding
        print(f"it a circle with radius {3.14* self.radius*self.radius}")
        super().describe()    

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height  

# Create objects
c = Circle("red", True, 5)
s = Square("blue", False, 6)      
t = Triangle("yellow", True, 3, 5)  

# Call describe method
c.describe()     # Output: It is red and filled.
s.describe()     # Output: It is blue and not filled.
t.describe()     # Output: It is yellow and filled.
