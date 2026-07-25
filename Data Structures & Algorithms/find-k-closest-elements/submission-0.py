class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        minHeap = []
        for a in arr:
            heapq.heappush(minHeap, [abs(a - x), a])
        
        result = []
        for _ in range(k):
            result.append(heapq.heappop(minHeap)[1])

        return sorted(result)