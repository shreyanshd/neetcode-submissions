class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for point in points:
            x, y = point[0], point[1]
            d = -(x ** 2 + y ** 2)
            heapq.heappush(maxHeap, (d,x,y))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        result = []
        for _ in range(k):
            d, x, y = heapq.heappop(maxHeap)
            result.append([x, y])
        return result