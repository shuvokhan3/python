class Message:
    x = 9
    y = 9


    def sum(self):
        return self.x + self.y

    @staticmethod
    def value():
        print('first value is : ',Message.x)

class commentMessage(Message):
    pass


# firstMessage = Message()
# firstCommentMessage = commentMessage()
#
# print(firstMessage.sum())
# print(firstCommentMessage.sum())

#direct access for static method
Message.value()
commentMessage.value()








