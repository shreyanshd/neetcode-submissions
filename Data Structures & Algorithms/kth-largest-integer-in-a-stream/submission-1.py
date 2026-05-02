class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = list(nums)
        heapq.heapify(self.minHeap)
        self.ensureSizeK()

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        self.ensureSizeK()
        return self.minHeap[0]
    
    def ensureSizeK(self):
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
