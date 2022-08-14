def topkelements(nums, k):
    # map1 = dict()
    # for i in range(len(nums)):
    #     map1[nums[i]] = map1.get(nums[i],0) + 1

    # print(map1.items())

    # for k,v in map1.items():
    #     print(map1[v])

    #     return None
    count = {}
    freq = [[] for i in range(len(nums)+1)]

    for n in nums:
        count[n] = 1 + count.get(n,0)
    print(count)


    for n,c in count.items():
        freq[c].append(n)
    
    print("freq is ",freq)
        
    res = []
    for i in range(len(freq)-1, 0, -1):
        for n in freq[i]:
            res.append(n)
            print(res)
            if len(res) == k:
                return res

#O(n)






nums = [1,1,1,2,2,3]
k = 2

topkelements(nums, k)