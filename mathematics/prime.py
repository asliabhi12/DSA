import math 
x = 67
def isPrime(x):
        m = int(math.sqrt(x))
        print(m)

        flag = 0
        for i in range(2, m+1):
            if x % i == 0:
                flag = 1

            if flag == 1:
                return False

        return True

print(isPrime(x))