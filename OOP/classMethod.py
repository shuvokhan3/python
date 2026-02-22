class MyClass :
    x = 10
    y = 23


    def addTwo(self,num1,num2):
        return self.x + self.y + num1 + num2



#create obj
obj = MyClass()
print(obj.addTwo(1,2))

