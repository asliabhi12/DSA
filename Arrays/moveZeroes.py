def moveZeroes(nums):
    count = 0

    for i in range(len(nums)):
        if nums[i] == 0:
            nums.remove(0)
            /nums.append(nums[i])
            count += 1

    for i in range(count):
        nums.append(0)
    


    return nums

print(moveZeroes([0,1,0,3,12]))