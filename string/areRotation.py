
def areRotation(s1, s2):
    if s1 == s2:
        return 1
    if len(s1) != len(s2):
        print("len was not same")
        return 0
    
    def leftrotate(s ,d):
        lFirst = s[0 : d]

        lLast = s[d :]

        return lLast + lFirst

    def rightrotate(s, d):
        rFirst = s[0 : len(s) -d]
        rLast = s[len(s) - d: ]

        return rLast + rFirst

    for i in range(len(s1)):
        if rightrotate(s1, i) == s2 or leftrotate(s1, i) == s2:
            return 1

    return 0

s1 = 'geeksforgeeks'
s2 = 'forgeek0geeks'  
 

print(areRotation(s1, s2))


