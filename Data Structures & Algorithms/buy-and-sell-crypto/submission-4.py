class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r= 0 , 1
        M=0
        while r<len(prices):
            if prices[r]-prices[l]<0:
                l=r
                r+=1
            else:
                M=max(prices[r]-prices[l],M)
                r+=1
        return M
