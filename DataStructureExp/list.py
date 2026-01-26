#list
value = ["apple", "banana", "cherry"]
print(value)
value.append("3433")
print(value)

#extend list
value_nex = ["apple", "banana", "cherry",1,2.3]
value.extend(value_nex)
print(value)

#removing value
print(value.remove("banana"))
print(value)

#delete value element wise
val = value.pop(2)
print(val)

#clear
# value.clear()

#index of the value
indexValue = value.index("banana")
print(indexValue)

#sorting list assending order
number = [123,24,3,45,5]
number.sort()
number.reverse()
print(number)

#list slicing
slicing_value = number[3:]
print(slicing_value)

#slicing list
value_slice = value[2:]
print(value_slice)

for val in value:
    print(val)
























