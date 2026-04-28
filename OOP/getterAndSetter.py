class Message:
    __firstComment = "This is a message"

    def __init__(self, text):
        self.__text = text

    def get_text(self):
        return self.__text

    def set_text(self, text):
        self.__text = text

    def get_first_comment(self):
        return self.__firstComment
    
    def set_first_comment(self, comment):
        self.__firstComment = comment
    

message = Message("Hello, World!")
print(message.get_text())  # Output: Hello, World!
message.set_text("Hello, Python!")
print(message.get_text())  # Output: Hello, Python!
print(message.get_first_comment())  # Output: This is a message 
message.set_first_comment("This is a new comment!")
print(message.get_first_comment())  # Output: This is a new comment!