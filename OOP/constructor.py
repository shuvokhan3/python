#constructor method __init__
class MyClass:
    x = 12
    y = 35
    def __init__(self,val1,val3):
        print(self.x + self.y)
        print(self.x + self.y + val1 + val3)




obj = MyClass(23,4)


#crete variable using constructor inside class
class Number:
    def __init__(self,val1,val2):
        self.x = val1
        self.y = val2


obj2 = Number(1,2)
print(obj2.x)
print(obj2.y)

