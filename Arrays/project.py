# list2d = [
#     [
#         [1,2,9,3,2,2]
#     ],
#     [
#         [2,6,9,3,2,2]
#     ],
#     [
#         [2,7,9,3,2,2,8,9]
#     ],
#     [
#         [1,5,7,3,7,5,9,3]
#     ]
# ]

# print(list2d[2][0])

print(ord("A")-ord("0"))
print(ord("a") - ord("0"))
arr = []
for c in range(97, 123):
    arr.append(chr(c))

fib = [0,1]
cur = 0
for i in range(2,26):
    fib.append((fib[i-1]) + (fib[i-2]))

print("fib len is ",len(arr))

print(fib)

print(arr)
hashmap = {}
for i in range(26):
    hashmap[arr[i]] = fib[i]

sum = 0
s = str(input())
s = s.lower()
print(hashmap["a"])
for c in s:
    sum += hashmap[c]

print("sum is ",sum)

print(hashmap)
