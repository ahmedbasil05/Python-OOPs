#multilevel inheritance = a class inherit from another inherited class
#         C(B) > B(A) > A

# Animal (Grandparent class) > Prey,Predator (Parent class) > Rabbit,Hawk,Fish (child class)

class Animal:    

    def __init__(self, name):
        self.name = name
        
    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")    

class Prey(Animal): 
    def flee(self):
        print("The animal is fleeing")

class Predator(Animal):
    def hunt(self):
        print("The animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey,Predator):
    pass

rabbit = Rabbit("bugs")  #object creation
hawk = Hawk("tony")
fish = Fish("nemo")

rabbit.eat()



