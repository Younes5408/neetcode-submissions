class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(ch.lower() for ch in s if ch.isalnum())
        r=len(s)-1
        l=0
        while r>=l:
            if s[r]!=s[l]:
                return False 
            else:
                r= r-1
                l= l+1
        return True