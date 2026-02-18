"""
key function

-json.dumps()
-json.loads()

"""

import json
import sys

#convert python obj to json string
# person = {
#     "name": "shuvo",
#     "age": 22,
#     "city": "dhaka"
# }
# personConvert = json.dump(person, sys.stdout)
# print(personConvert)


#convert json to python object
personJson = '{"name": "John", "age": 5}'
personObj = json.loads(personJson)
print(personObj)

print("first name is :", personObj['name'])


