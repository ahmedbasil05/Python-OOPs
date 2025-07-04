#abstract class = a class that cannot be instantiated on its own, meant to be subclasssed
#               we cant create objects on our own, we have to do it in inherited class
#               we define the abstract methods in the child class
#               They can contain abstract methods, which are declared but have no implementation
#               1. Prevents instantiaion of the class itself
#               2. Requires children to use inherited abstract methods

from abc import ABC, abstractmethod

class Vehicle(ABC):   #parent class

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):    #child class
    def go(self):      #method overriding
        print("you are driving a car")

    def stop(self):
        print("you are stopping the car")   

class Motorcycle(Vehicle):   #child class
    def go(self):
        print("you ride the bike")

    def stop(self):
        print("you stop the bike")     




car = Car()
car.go()
car.stop()    

motor = Motorcycle()
motor.go()
motor.stop()
