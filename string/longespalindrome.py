def longestPalin(S):
        # code here
        resLen = 0
        res =""
        for i in range(len(S)):
                l, r = i, i
                #for odd
                while l >= 0 and r < len(S) and S[l] == S[r]:
                    if (r - l + 1) > resLen:
                        resLen = r - l+ 1
                        res = S[l:r+1]
                    l -=1
                    r += 1
                l, r = i, i + 1
                #for even

                while l >= 0 and r < len(S) and S[l] == S[r]:
                    if (r - l + 1) > resLen:
                        resLen = r -l +1
                        res = S[l:r+1]
                    l -=1
                    r += 1
        return res


print(longestPalin('aabbaambba'))