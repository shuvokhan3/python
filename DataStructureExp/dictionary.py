#dictionary data
person = {
    "name" : "Rahim",
    "age" : 22,
    "height" : 70
}

print(person.items())
#update dictionary
person.update({'name':'shuvo'})
print(person.items())

#pop value
person.pop('name')
print(person.items())

