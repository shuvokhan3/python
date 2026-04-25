class car :

    #public access modifier
    brand = "BMW"

    def Display(self):
        print(self.brand)

class bus:
    #protected access modifier
    _brand = "Volvo"

    def Display(self):
        print(self._brand)

class bike:

    #private access modifier
    __brand = "Honda"

    def Display(self):
        print(self.__brand)

    

    
#public access modifier
obj = car()
obj.Display()

#protected access modifier
obj1 = bike()
obj1.Display()

#private access modifier
obj2 = bus()
obj2.Display()
