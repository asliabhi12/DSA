fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

# newlist = [expression for item in iterable if condition == True]

newlist = [x for x in fruits if "a" in x]

print(newlist)             

newlist =  [x for x in fruits]

print(newlist)             

newlist = [x for x in range(10) if x <5] 
print(newlist)             
