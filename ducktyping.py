#Ducktyping = another way to achieve polymorphism besides inheritance
#           obj must have minimum necessary attributes/methods
#           "if it looks like a duck and quacks like a duck, it must be a duck"

class Animal:
    alive = True

class Cat(Animal):
    def speak(self):
        print("meow meow")

class Dog(Animal):
    def speak(self):
        print("dog barks") 

animals = [Cat(), Dog()]                   

for animal in animals:
    animal.speak()