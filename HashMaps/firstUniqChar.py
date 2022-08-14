def firstUniqChar(s):
    hashmap = dict()

    for i, char in enumerate(s):
        print("char is", i)
        print("hash map at i iterations :",hashmap)
        if char in hashmap:
            hashmap[char] = [hashmap[char][0], hashmap[char][1] + 1]
            print('as char was in hashmap new hash  map looks like', hashmap)


        else: 
            hashmap[char] = [i, 1]
            print('char wasnt in hashmap so', i)

        for key, value in hashmap.items():
            if value[1] == 1:
                return value[0]

        return -1

print(firstUniqChar('ssaabbkccm'))

