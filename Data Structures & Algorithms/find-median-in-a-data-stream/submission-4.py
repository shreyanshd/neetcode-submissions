class MedianFinder:

    def __init__(self):
        self.maxheap = []
        self.minheap = []

    def addNum(self, num: int) -> None:
        if self.minheap and num > self.minheap[0]:
            heapq.heappush(self.minheap, num)
        else:
            heapq.heappush(self.maxheap, -num)
        
        if len(self.maxheap) > len(self.minheap) + 1:
            elem = -heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, elem)
        if len(self.minheap) > len(self.maxheap) + 1:
            elem = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -elem)

    def findMedian(self) -> float:
        if len(self.maxheap) == len(self.minheap):
            return (-self.maxheap[0] + self.minheap[0]) / 2
        elif len(self.maxheap) > len(self.minheap):
            return -self.maxheap[0]
        else:
            return self.minheap[0]