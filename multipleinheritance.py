#multiple inheritance = inherit from more than one class
#                      C(A,B)

class Prey:

    def __init__(self, name):
        self.name = name
        
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator:

    def __init__(self, name):
        self.name = name
        
    def hunt(self):
        print(f"{self.name} is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey,Predator):   #multiple inheritance
    pass

rabbit = Rabbit("rabbit")  #object creation
hawk = Hawk("hawk")
fish = Fish("fish")

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()

