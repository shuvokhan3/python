#declared set
data = {22,3,5,6}
dataTwo = {22,33,54,65}

#add a new value inside set
data.add(8)

#remove element from set
# data.remove(2)

#union two set
res = data.union(dataTwo)
print(res)

#intersection point of two set
res = data.intersection(dataTwo)
print(res)


#difference
res = data.difference(dataTwo)
print(res)

res = data.issubset(dataTwo)
print(res)

res = data.issuperset(dataTwo)

