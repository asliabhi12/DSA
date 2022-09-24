numbers = int(input())
list = list(map(int,input("\n enter the number").strip().split()))[:numbers]
 # Reading input from STDIN
def fizzBuzz(n):
    for j in range(1, n+1):
        if j%3 ==0 and j % 5==0:
            print("FizzBuzz")
        elif j % 3 == 0:
            print("Fizz")
        elif j % 5 == 0:
            print("Buzz")
        else:
            print(j)

for m in range(len(list)):
    fizzBuzz(list[m])
