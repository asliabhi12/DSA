def fastPower(a, b):
    res = 1
    stage = 0
    while(b > 0):
        stage += 1
        print("at stage ", stage, ": b =", b)
        if(b & 1) != 0:
            res = res * a    
            ("it was divisble by 2, so res =", res)    
        a = a * a
        print("a is", a)
        b = b >> 1
        print("b is", b)  
    return res 


print(fastPower(3, 5))