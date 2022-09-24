rows = int(input())

for i in range(rows):
    for j in range(i+1):
        if i% 2 == 0:
            if j%2==1:
                print("0", end="")
            else:
                print("1",end="")
        else:
            if j%2==0:
                print("0",end="")
            else:
                print("1", end ="")

    print("")