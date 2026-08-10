class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k== 1:
            return max(nums)
        a=[]
        heapq.heapify(a)
        for i in nums:
          heapq.heappush(a,i)
        while len(a)> k:
            heapq.heappop(a)
        return a[0]