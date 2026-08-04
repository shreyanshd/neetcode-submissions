class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = []
        for point in points:
            x, y = point[0], point[1]
            dist = math.sqrt(x**2 + y**2)
            heapq.heappush(maxheap, (-dist, x, y))
            if len(maxheap) > k:
                heapq.heappop(maxheap)
        
        output = []
        while maxheap:
            d, x, y = heapq.heappop(maxheap)
            output.append([x, y])
        return output