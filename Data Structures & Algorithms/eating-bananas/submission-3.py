class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k=max(piles)-1
        if len(piles) == h:
            return max(piles)
        l,r = 1, max(piles)
        
        while l<=r:
             mid= (l+r)//2
             n=0
             for x in piles :
                n+= math.ceil(float(x)/mid) 
             if n>h:
                l=mid+1
             else :
                r= mid-1
                a=mid
        return a