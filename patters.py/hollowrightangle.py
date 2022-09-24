rows = int(input())

for i in range(rows):
    for j in range(i+1):
        if i == j or j == 0 or i == rows-1:
            print("*", end="")
        else:
            print(" ", end = "")
    print("")