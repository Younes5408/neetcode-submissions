class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        a=[]
        for x,y in points:
            d=pow(x,2)+pow(y,2)
            heapq.heappush(a,(-d,[x,y]))
        while len(a)>k:
            heapq.heappop(a)
        return [c for y,c in a ]

