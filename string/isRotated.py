def isRotated(str1,str2):
        if len(str1) != len(str2):
            return 0
        right  = str1
        left = ""
        for i in range(2):
            right += (str1[i])


        
        for i in range(len(str1)- 1, len(str1) - 3, -1):
            left = (str1[i]) + left
        left+= str1
        



        if right[2:] == str2 or left[:-2]:
            return 1
        else: 
            return 0

a = "amazon"
b = "azonam"
print(isRotated(a, b))