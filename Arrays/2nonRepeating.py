def onlyNonRepeating(nums):
    res = 0
    for i in range(0,len(nums)):
        res = res ^ nums[i]

    res = res & -res

    sum1 = 0
    sum2 = 0

    for i in range(0, len(nums)):
        if nums[i] & res > 0:
            sum1 = sum1 ^ nums[i]

        else:
            sum2 = sum2 ^ nums[i]

    return [sum1, sum2]

a = [2, 4, 7, 9, 2, 4]


print(f'only two non repeating element is:',onlyNonRepeating(a))