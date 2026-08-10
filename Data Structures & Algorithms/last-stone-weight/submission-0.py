class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones= [-s for s in stones]
        heapq.heapify(stones)

        while len(stones)>1:
            M1= min(stones)
            heapq.heappop(stones)
            M2= min(stones)
            heapq.heappop(stones)
            heapq.heappush(stones , -abs(M1-M2))
        
        if stones:
            stones = [-s for s in stones]
            return stones[0]
        else:
            return 0


        