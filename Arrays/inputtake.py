# lst =[]
# n = int(input("number of elements"))

# for i in range(n):
#     ele = input()
#     lst.append(ele)

# print(lst)

# with handling Exceptions

# try:
#     myList = []

#     while True:
#         myList.append(int(input()))

# except:
#     print(myList)


#using map

# n = int(input("number of elements"))
# a = list(map(int,input("Enter the numbers ").strip().split()))[:n]

# print(a)


#list of list as input

# lst = []
# n = int(input("enter number of elements: "))

# for i in range(n):
#     ele = [input(), int(input())]
#     lst.append(ele)

# print(lst)

lst1 = []  
  
# For list of strings/chars
lst2 = []  
  
lst1 = [int(item) for item in input("Enter the list items : ").split()]
  
lst2 = [item for item in input("Enter the list items : ").split()]
  
print(lst1)
print(lst2)

