class MyClass:
    num1 = 1
    num2 = 2
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @staticmethod
    def sum():
        return MyClass.num1 + MyClass.num2


#access static method
print(MyClass.sum())

#using creating obj i also access static method
obj = MyClass(2,3)
print(obj.sum())


