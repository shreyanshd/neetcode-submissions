class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: (interval[1]))
        latest = intervals[0]
        valid = 1
        print(intervals)
        for i in range(1, len(intervals)):
            if latest[1] <= intervals[i][0]:
                latest = intervals[i]
                valid += 1
        return len(intervals) - valid
        