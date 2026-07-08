class Solution:
    def trap(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        ml,mr,v=0,0,0
        a=0


        while l<r:
            ml,mr=max(ml,height[l]),max(mr,height[r])
            if ml<mr:
                l+=1
                a=ml- height[l]
                if a<0:
                   a=0
                v+=a
            else:
                r-=1
                a=mr-height[r]
                if a<0:
                  a=0
                v+=a
        return v
           
