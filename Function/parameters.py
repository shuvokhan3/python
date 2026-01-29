def sum(num1, num2):
    print(num1 + num2)

sum(1, 2)

print("varible -length arguments")
#variable-length Arguments(*arg) Tuples
def multiply(*values):
    multiplier = 1
    for value in values:
        multiplier *= value

    print(multiplier)


multiply(1, 2,2,5)


#keyword Argument (when send parameter in dictionary)
def data(**value):
    print(value)
data(name='sh',age=20)

