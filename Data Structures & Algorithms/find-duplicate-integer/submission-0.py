class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s,f= 0,0
        while True:
            s,f= nums[s],nums[nums[f]]
            if s == f:
                break
        
        s2= 0
        while True:
            s2, s =nums[s2] , nums[s]
            if s2 == s:
                return s2