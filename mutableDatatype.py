#create a list
listData = [1,2,3,4,5]
fist_location = id(listData)
print(fist_location)

#chage the value of index 0
listData[0] = 23
last_location = id(listData)
print(last_location)

print(listData)