from collections import Counter
def canConstruct(ransomNote: str, magazine: str) -> bool:
        dic1 = Counter(ransomNote)
        dic2 = Counter(magazine)
        for k in dic1:
            if k not in dic2 or dic2[k] < dic1[k]:
                return False
        return True

print(canConstruct("aabcllvdck", "aabcck"))