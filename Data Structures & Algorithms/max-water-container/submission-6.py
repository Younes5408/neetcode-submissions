class Solution:
    def maxArea(self, heights: List[int]) -> int:
      l,r=   0,len(heights)-1
      v=0

      while r>l:
        a=min(heights[r],heights[l])
        d= r-l
        v=max(v,a*d)
        if heights[r]>heights[l]:
            l+=1
        else:
            r-=1
      return v  



