"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
            
        minHeap = [(i.start, i.end) for i in intervals]
        heapq.heapify(minHeap)
        cur = heapq.heappop(minHeap)
        while minHeap:
            nxt = heapq.heappop(minHeap)
            if cur[1] > nxt[0]:
                return False
            cur = nxt
        return True
