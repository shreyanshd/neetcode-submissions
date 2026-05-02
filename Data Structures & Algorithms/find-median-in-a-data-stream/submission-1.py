class MedianFinder:

    def __init__(self):
        self.median = None
        self.count = 0
        self.left = [float('inf')]  # max heap
        self.right = [float('inf')] # min heap

    def addNum(self, num: int) -> None:
        if self.count % 2 == 0:
            if num > self.right[0]:
                self.median = heapq.heappop(self.right)
                heapq.heappush(self.right, num)
            elif num < -self.left[0]:
                self.median = -heapq.heappop(self.left)
                heapq.heappush(self.left, -num)
            else:
                self.median = num
        else:
            if self.median < num:
                heapq.heappush(self.left, -self.median)
                heapq.heappush(self.right, num)
            else:
                heapq.heappush(self.left, -num)
                heapq.heappush(self.right, self.median)
            self.median = None
        self.count += 1

    def findMedian(self) -> float:
        if self.count % 2 == 0:
            return (-self.left[0] + self.right[0]) / 2
        else:
            return self.median
        