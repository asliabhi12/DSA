def fastPower(x, n):
    res = 1
    if n < 0:
        n = abs(n)
        x = 1/ x
        print(x)
    while(n > 0):
        print("this is n & 1==",n&1)
        if(n & 1) != 0:
            res = res * x    
        x = x * x
        print("here x is", x)
        n = n >> 1  
    return res 

print(fastPower(1455, -2))