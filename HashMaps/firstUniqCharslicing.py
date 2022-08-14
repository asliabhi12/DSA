def firstUniqChar(s: str) -> int:
        for i in range(len(s)):
            if s[i] not in s[:i] and s[i] not in s[i+1:]:
                return i
            
        else:
            return -1


print(firstUniqChar('ssaabbcc'))