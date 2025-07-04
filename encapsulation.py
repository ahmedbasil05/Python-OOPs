#Encapsulation = one of the key features of oop.
#             refers to bundling of attributes and methods inside a single class
#    it prevents outer class from accessing and changing attributes and methods. also help achieve data handling

class Person:
    def __init__(self, name, age):
        self.name = name            # public
        self.__age = age            # private

    def show(self):
        print(f"Name: {self.name}, Age: {self.__age}")

    def set_age(self, new_age):
        if new_age > 0:
            self.__age = new_age    # controlled access
        else:
            print("Invalid age")

    def get_age(self):
        return self.__age

p = Person("Alice", 30)
p.show()

print(p.name)         # ✅ Public: works
# print(p.__age)      # ❌ Private: raises AttributeError
print(p.get_age())    # ✅ Use getter

p.set_age(35)         # ✅ Use setter
print(p.get_age())    # 35
