class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        m=max(piles)
        l,r=1,m
        while r>=l:
            k=(r+l)//2
            n=0
            for i in piles:
                n+=math.ceil(float(i) /k)
            if n>h:
                l=k+1
            else:
                r=k-1
                a=k
        return a

