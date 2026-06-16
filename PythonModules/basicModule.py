# math module :provide mathamatical operations

import math

print(math.sqrt(13))
print(math.pi)
print(math.cos(0))
print(math.sin(0))
print(math.tan(0))
print(math.log(10))


# random module : provide random number generation
print("\n")
import random
print(random.random())  # random float between 0 and 1
print(random.randint(1, 10))  # random integer between 1 and 10

#os module : provide functions for interacting with the operating system
import os
print(os.getcwd())  # get current working directory
print(os.listdir())  # list files in current directory  

import datetime
# datetime module : provide classes for manipulating dates and times
now = datetime.datetime.now()

#json module
import json
# json module : provide functions for working with JSON data
data = {"name": "Alice",
         "age": 30,
         "city": "Dhaka"
   }

json_data = json.dumps(data) # convert Python object to JSON string
print(json_data)

