#Multiple inharitance

class Message:

    totalMessage = 34

    def __init__(self, name, message):
        self.name = name
        self.message = message

    def personMessage(self):
        print(self.name, self.message)

    def TotalNumberOfMessages(self):
        print("Total Message is : ", self.totalMessage)

class PictureMessage:
    def __init__(self, name, message):
        self.name = name
        self.message = message

    def PictureMessage(self):
        print(self.name, self.message)



class CommentMessage(Message, PictureMessage):
    pass





#child class obj
firstCommentMessage = CommentMessage("firstCommentMessage", "first comment")
firstCommentMessage.TotalNumberOfMessages()

firstCommentMessage.PictureMessage()

