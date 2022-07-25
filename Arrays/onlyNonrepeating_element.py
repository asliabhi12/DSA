
def onlyNonRepeating(nums):
    res = 0
    for i in range(0,len(nums)):
        res = res ^ nums[i]

    return res

a = [5, 4, 1, 4, 3, 3, 9, 5, 1]


print(f'only non repeating element is:',onlyNonRepeating(a))