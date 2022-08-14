


def ransomNote(s, t):
    map1 = dict()
    map2 = dict()
    for i in range(len(t)):
        map1[t[i]] = map1.get(t[i],0) + 1
    print("map1 has ",map1)

    for i in range(len(s)):
        map2[s[i]] = map2.get(s[i],0) + 1
    print("map2 has ",map2)

    flag = 0
    
    print(map1.items())

    

    for k,v in map1.items():
        print(k)
        print(map2[k])
        if k in map2 and map1[k] <= map2[k]:
            flag =1
        else:
            flag = 0
            break
    if flag:
        return True
    return False


    
    
print(ransomNote("aabcllvdck", "aabcck"))


        
