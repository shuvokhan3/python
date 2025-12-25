#int datatype
from numba.core.cgutils import is_true
from pydantic_core.core_schema import none_schema

age = 3
print(age)
age = age + 1
print(age)
print(age)




#float datatype
res = 22.3
print(type(res))

#complex number
complex_number = 20+34j
print(complex_number)

#string datatype
name = "shuvo"
print(name)

#Sequence datatype


#list datatype (mutable datatype)
city=["Dhaka", "kulna", "Barshal"]
value = [1,2,3,4,5]
print(type(value))
print(city)

name = ["rahim", "karim"]
print("First Name",name)
name[0] = "shuvo"
print("Change Name", name)





#tuple datatype
numbers = ("A", "B", "C", "D", "E", 2)
print(numbers)
print(type(numbers))

#range datatype
val1 = range(1,20)
print(*val1)

val3 = range(1,10,2)
print(*val3)

val4 = range(10)
print(*val4)

#bool datatype
val5 = True
print(val5)

#none type
no = None
print(no)

#mapping datatype
#dict type
# idInfo = {
#     "name" : "shuvo",
#     "age" : 34,
#     "number" : "123222322"
# }
#
# print(idInfo['name'])
#

""""""
#set types( set avoid duplicate value )
num = {1,2,2,3,5}
print(num)
""""""

""""""
#frozenset(frozenset also avoid duplicate value
num2 = frozenset({1,2,2,3,5})
print(num2)
""""""









