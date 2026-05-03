"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        points = [(i.start, True) for i in intervals] + [(i.end, False) for i in intervals]
        points.sort(key = lambda x: (x[0], x[1]))
        rooms, minRooms = 0, 0
        for p in points:
            add = 1 if p[1] else -1
            rooms += add
            minRooms = max(rooms, minRooms)
        return minRooms


