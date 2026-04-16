class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        heap = []
        for n in count.keys():
            f = count[n]
            heapq.heappush(heap, (f, n))
            if len(heap) > k:
                heapq.heappop(heap)
            
        res = []
        for i in range(k):
            n = heapq.heappop(heap)[1]
            res.append(n)
        return res