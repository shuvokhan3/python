class Message:
    x = 9
    y = 999
    def sum(self):
        return self.x + self.y

    @staticmethod
    def value():
        print('first value is : ',Message.x)
class commentMessage(Message):

    def addTwo(self):
        print('Number is : ',self.x, self.y,self.sum())


firstMessage = Message()

firstCommentMessage = commentMessage()
print(firstMessage.sum())
print(firstCommentMessage.sum())
firstCommentMessage.addTwo()


#direct access for static method
Message.value()
commentMessage.value()










