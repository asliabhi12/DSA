class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 0, n
        while l <= r:
            mid = (l +  r)//2
            if isBadVersion(mid):
                if not isBadVersion(l): return mid
                
            elif isBadVersion(mid)
                
            else:
                l = mid + 1
                
            