class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a= set()
        l,M=0,0
        for r in range(len(s)):
            while s[r] in a:
                a.remove(s[l])
                l+=1
            a.add(s[r])
            r+=1
            M=max(M,r-l)
        return M