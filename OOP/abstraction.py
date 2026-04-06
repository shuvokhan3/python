from abc import ABC, abstractmethod

class Student(ABC):
    @abstractmethod
    def address(self):
        pass
    @abstractmethod
    def name(self):
        pass
    @abstractmethod
    def score(self):
        pass

class Student2(Student):
    def address(self):
        print("Nazirpur , Dhirjan , ruhitalabunia")

    def name(self):
        print("raisul islam")

    def score(self):
        print("33")

val = Student2()
val.address()


val.name()
val.score()