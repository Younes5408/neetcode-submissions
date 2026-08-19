class Solution:
    def search(self, nums: List[int], target: int) -> int:
        r,l=len(nums)-1,0
        while r>=l:
            m=(r+l)//2
            if nums[m]>target:
                r=m-1
            elif nums[m]<target:
                l=m+1
            else:
                return m
        return -1
