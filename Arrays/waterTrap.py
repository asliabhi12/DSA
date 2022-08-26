
def trap(height):
    leftbig = 1
    rightbig = height[-1]
    left = []
    right = []
    res = []
    for i in range(len(height)):
        if height[i] > leftbig:
            leftbig = height[i]

        left.append(leftbig)

    for j in range(len(height)-1, -1, -1):
        if height[j] > rightbig:
            rightbig = height[j]

        right.insert(0, rightbig)
        
    for i in range(len(height)):
        res.append(min(left[i],right[i])-height[i])

        
        


    print("left =",left)
    print("right =",right)
    print("result = ", res)

trap([3,1,2,4,0,1,3,2])




