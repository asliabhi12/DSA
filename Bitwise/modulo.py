def fastPower(x, n):
    res = 1

    if n < 0:
        n = abs(n)
        x = 1/ x


    while(n > 0):
        if(n & 1) != 0:
            res = res * x    
        x = x * x
        n = n >> 1
        



    
    return res 


print(fastPower(2.00000, -2))