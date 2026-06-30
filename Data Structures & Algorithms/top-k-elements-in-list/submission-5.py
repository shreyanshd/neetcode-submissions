class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        for elem, f in count.items():
            heapq.heappush(heap, (f, elem))
            if len(heap) > k:
                heapq.heappop(heap)
        ret = [elem for f, elem in heap]
        return ret