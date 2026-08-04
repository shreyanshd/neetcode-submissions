class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-s for s in stones]
        heapq.heapify(maxheap)
        while len(maxheap) > 1:
            s1 = heapq.heappop(maxheap)
            s2 = heapq.heappop(maxheap)
            if s1 != s2:
                heapq.heappush(maxheap, s1 - s2)
        return -maxheap[0] if len(maxheap) == 1 else 0
        