#method overloading
class comment:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2
    #use default parameter i create method overloading
    def add(self,num1 = 0, num2 = 0):
        self.value1 = num1
        self.value2 = num2
        print(self.value1 + self.value2)

    #use this * i can send unlimited paramenter
    def mess(self, *a):
        print(a)



cal = comment(22,2)
cal.add()
cal.mess(2,33,3)



