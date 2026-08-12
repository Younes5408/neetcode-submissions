class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-s for s in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            R1=heapq.heappop(stones)
            R2=heapq.heappop(stones)
           
            heapq.heappush(stones,-abs(R1-R2))
        
        stones = [-s for s in stones]
        return stones[0]



        