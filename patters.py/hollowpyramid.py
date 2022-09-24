n = int(input())

for i in range(n):
    for j in range(n - i -1):
        print(" ", end = "")

    for j in range(i*2 + 1):
        if j == 0 or j == 2*i or i == n-1:

            print("*", end="")

        else:
            print(" ", end = "")
    print()