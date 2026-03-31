class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def address(self):
        print(self.name, self.age)


class ClassOne(Student):
    #Overriding
    def address(self):
        print(self.name, self.age)

#create obj for parent class
name = Student("John", 22)
name.address()

#create  obj for child class
anotherName = Student("shuvo", 25)
anotherName.address()
