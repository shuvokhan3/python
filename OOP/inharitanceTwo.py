class Father:
    x = 23
    y = 45

    def __init__(self):
        print("Father's constructor")

    def add(self):
        print(self.x + self.y)

    def mul(self):
        print(self.x * self.y)


class Son(Father):
    pass

#create two object for class
#here i show that son also access the father constructor
obj = Father()
obj2 = Son()
