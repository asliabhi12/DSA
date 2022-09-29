# Dictionaries are used to store data values in key:value pairs.

# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

# thisdict = {
#   "model": "Mustang",
#   "year": 1964
# }

# print(thisdict.get("brand"))


# # no duplicates allowed


# print(thisdict)

# print(len(thisdict))

# print(type(thisdict))

# x = thisdict.keys() 
# print(x)

import this


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

# x = car.keys()

# print(x) #before the change

# car["color"] = "white"

# print(x) #after the change 

# x = car.values()
# print(x)


# car["year"] = 2021


# car["color"] = "red"


# print(car.items())

# print(car.popitem())

# print(car.items())
# print(car)
# del car
# print(car)

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)

print(thisdict)

# x = thisdict.fromkeys("brands")
# print(x)

# # print("keys: ")
# # for x in thisdict:
# #   print("   " + x) 
# # print("values: ")
# # for x in thisdict.values():
# #   print("   ",  x) 

# for x in thisdict.keys():
#     print(x)

# for x, y in thisdict.items():
#   print(x,"-", y) 


# mydict = thisdict.copy()

# print(mydict)


# yourdict = dict(mydict)

# print(yourdict)

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
} 




print(myfamily["child1"]["name"])













