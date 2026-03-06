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
    def __init__(self):
        #call the parent constructor
        super().__init__()
        print("Son's constructor")



obj2 = Son()
