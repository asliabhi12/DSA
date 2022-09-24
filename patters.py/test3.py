import re
x = input()
n = int(input())
a=""

letters = re.split("[0-9]+", x)
letters.remove('')
numbers = re.split("[a-z]+", x)
numbers.remove('')
numbers = list(map(int, numbers))
for i in range(len(letters)):
    a += letters[i]*numbers[i]

if len(a) > n:
    print(a[n])
else: print(-1)





