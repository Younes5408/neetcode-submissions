class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1
        s=0
        while l<r:
            s1,s2=heights[l],heights[r]
            h=min(s1,s2)
            s= max(s,h*(r-l))
            if s1>s2:
                r-=1
            else:
                l+=1
        return s