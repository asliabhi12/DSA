# def isAnagram(a,b):
#         #code here
#         if len(a) != len(b):
#             return False
        
#         dictA, dictB = {}, {}
        
#         for i in range(len(a)):
#             dictA[a[i]] = 1 + dictA.get(a[i], 0)
#             dictB[b[i]] = 1 + dictB.get(b[i], 0)
            
#         for c in dictA:
#             if dictA[c] != dictB.get(c,0):
#                 return False
                
#         return True

a = "hello"
sorted(a)

arr = ["geeksforgeeks", "geeks", "geek","geezer"]


x = ""
for i in range(1, len(arr)):
    for j in range(len(min(arr))):
        if arr[i][j] == arr[i-1][j]:
            continue
    print(arr[i:j], end ="")
            





