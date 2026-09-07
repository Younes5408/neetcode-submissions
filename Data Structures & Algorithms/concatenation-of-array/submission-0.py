class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[0]*(2*n)
        for i, na in enumerate(nums):
            ans[i]= ans[i+n] = na
        return ans
        
