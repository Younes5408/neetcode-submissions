class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       m={}
       for i,a in enumerate(nums):
          if target-a in m :
               return [m[target-a] , i]
          m[a]=i

