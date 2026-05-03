"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        points = []
        for i in intervals:
            points.append((i.start, 1))
            points.append((i.end, -1))
        
        points.sort(key = lambda x: (x[0], x[1]))
        
        rooms, minRooms = 0, 0
        for p in points:
            rooms += p[1]
            minRooms = max(rooms, minRooms)
        return minRooms


