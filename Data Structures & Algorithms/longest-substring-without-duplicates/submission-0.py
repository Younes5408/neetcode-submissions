class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a= set()
        r,l,M=0,0,0
        while r<len(s):
            if s[r] not in a :
                a.add(s[r])
                r+=1
                M=max(M,r-l)
            else:
                dele= s[r]
                while s[l] != dele:
                    a.remove(s[l])
                    l+=1
                a.remove(s[l])
                l+=1
        return M

