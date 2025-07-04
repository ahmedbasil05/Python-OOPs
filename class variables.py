#class variables = shared among all instances of class
#                  defined outside the contructor
#                  allow to share data among all objects created from that class

class Student:

    class_year = 2025     #class variable
    num_students = 0

    def __init__(self, name, age):
        self.name = name  #instance variables
        self.age = age
        Student.num_students +=1

s1 = Student("abc", 15)
s2 = Student("xyz", 18) 
s3 = Student("pqr", 25)

print(s1.age)
print(Student.class_year)   #acess class variable with class name
print(Student.num_students)   

print(f"my graduating class of {Student.class_year} has {Student.num_students} students")
print(s1.name)
print(s2.name)
print(s3.name)