#Polymorphism  = greek word that means to "have many forms"
#              poly - many
#              morphe - forms

#        Two ways to achieve polymorphism
#        Inheritance = an obj could be treated of same type as a parent class
#        "Duck Typing" = obj must have unnecessary attributes/methods

from abc import ABC, abstractmethod

class Shape:

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):  #method overriding
        return 3.14 * self.radius **2 
    

class Square(Shape):  
     def __init__(self, side):
        self.side = side

     def area(self): #method overriding - aparent class function is override by a child class
        return self.side ** 2
     
c = Circle(3)
s = Square(4)

print(c.area())
print(s.area())
   
          
