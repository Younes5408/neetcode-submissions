class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setu= set()
        for i in nums:
            if i not in setu:
                setu.add(i)
            else:
                return True

        return False