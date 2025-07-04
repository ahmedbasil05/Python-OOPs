#Inheritance = allows a class (child) to inherit attributes and methods from another (parent) class
#              helps with reusability and extensibility
#              class Child(Parent)

class Animal: #parent class
    def __init__(self,name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):  #child class
    def bark(self):
        print("Barks!!")

class Cat(Animal):  #child class
    def meow(self):
        print("meow!!")

dog = Dog("miru")   #object
cat = Cat("bella")  #object 

print(dog.name)
print(dog.is_alive)
dog.sleep()
dog.bark()
cat.meow()