#single inharitance
class Message:
    def __init__(self, name, message):
        self.name = name
        self.message = message

    def personMessage(self ):
        print(self.name, self.message)

class CommentMessage(Message):
    pass


#parent class obj
firstMess = Message("firstMess", "first message")
firstMess.personMessage()

#child class obj
firstCommentMessage = CommentMessage("firstCommentMessage", "first comment")
firstCommentMessage.personMessage()

