#Create file
#write file
with open("example.text","w") as file:
    file.write("Bangladesh is an independent country")


#Read file
with open("example.text","r") as file:
    content = file.read()
    print(content)

#rename file
import os
os.rename("example.text","example2.txt")

#remove file
os.remove("fileDirectory/example.txt")




