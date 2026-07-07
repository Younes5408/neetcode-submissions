class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        Mp=0
        while r<len(prices):
            P=prices[r]-prices[l]
            if P<0:
                l=r
            r+=1
            Mp=max(P,Mp)
        return Mp
