class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for point in points:
            x, y = point[0], point[1]
            d = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
            minHeap.append((d, x, y))
        
        heapq.heapify(minHeap)

        result = []
        for _ in range(k):
            d, x, y = heapq.heappop(minHeap)
            result.append([x, y])
        return result