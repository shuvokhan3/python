class Father:
    x = 34
    y = 54

    #without creating any object this class able to access this method
    @staticmethod
    def add():
        print(Father.x + Father.y)

    @staticmethod
    def mess():
        print("This is a message from Father class")

class Son(Father):
    pass


Son.add()






