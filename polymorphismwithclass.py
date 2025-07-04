class Dog:
    def sound(self):
        return "Bark"

class Cat:
    def sound(self):
        return "Meow"

# Common interface
def animal_sound(animal):
    print(animal.sound())

d = Dog()
c = Cat()

animal_sound(d)  # Bark
animal_sound(c)  # Meow
