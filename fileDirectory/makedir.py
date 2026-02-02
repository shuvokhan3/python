import os

os.makedirs("mkdir", exist_ok=True)

# with open("mkdir/test.txt", "w") as file:
#     file.write("Bangladesh is an independent country")

file_list = os.listdir("mkdir")
print(type(file_list))