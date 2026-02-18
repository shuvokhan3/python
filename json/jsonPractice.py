"""
key function

-json.dumps()
-json.loads()

"""

import json
import sys

#convert python obj to json string
person = {
    "name": "shuvo",
    "age": 22,
    "city": "dhaka"
}
personConvert = json.dump(person, sys.stdout)
print(personConvert)




