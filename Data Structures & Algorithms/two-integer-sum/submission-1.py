class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       a={}
       for i,m in enumerate(nums):
            if target-m in a:
                return [a[target-m],i]
            a[m]=i