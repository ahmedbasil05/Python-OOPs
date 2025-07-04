# object - A "bundle" of related attributes (variables) and methods (fucntions)
#        ex - fan, AC, book
# class = (blueprint) used to design structure and layout of an object

class Car:
    def __init__(self, model, year, color, for_sale):     #attributes
        self.model = model  #instance variables - inside the constructor
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print("driving the car")  

    def stop(self):         #methods
        print("stop the car")   

    def describe(self):
        print(f"{self.model} is {self.year} and color is {self.color} and is for {self.for_sale}")       

car1 = Car("reborn", 2014, "silver", False)  #objects
car2 = Car("yaris", 2020, "gray", True)   

print(car1)
print(car2.model)

car1.describe()
car2.describe()