# def checkInculsion(s1,s2):
#     if len(s1) > len(s2): return False

#     s1count, s2count = [0] * 26, [0] * 26
#     for i in range(len(s1)):
#         s1count[ord(s1[i]) - ord('a')] += 1
#         s2count[ord(s2[i]) - ord('a')] += 1
#     print(s2count)

#     matches = 0
#     for i in range(26):
#         matches += 1 if s1count[i] == s2count[i] else 0


#     l = 0 
#     for i in range(len(s1), len(s2)):
#         if matches == 26:
#             return True
        
#         index = ord(s2[r]) - ord('a')






def checkInclusion( s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_map = {}
        s2_map = {}
        for i in range(ord('a') , ord('z') + 1):
            s1_map[chr(i)] = 0
            s2_map[chr(i)] = 0

        
        
        for i in s1:
            s1_map[i] += 1

        print(s2[0])
            
        l = 0
        r = 0
        
        while r < len(s2):
            if r == 0:
                while r < len(s1):
                    s2_map[s2[r]] += 1
                    r += 1
                if s2_map == s1_map:
                    return True

            else:
                s2_map[s2[l]] -= 1
                s2_map[s2[r]] += 1
                
                if s2_map == s1_map:
                    return True
                else:
                    l += 1
                    r += 1
            
        return False  



print(checkInclusion('abcd', 'eabdck'))

