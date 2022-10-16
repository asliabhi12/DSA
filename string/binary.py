def binary(str):
   
    for e in range(1, len(str)):
        if str[e] != '0' and str[e] != '1':
           return 0
    return 1

str = "101"
print(binary(str))


