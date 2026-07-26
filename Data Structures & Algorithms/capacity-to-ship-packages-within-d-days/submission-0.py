class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        result = r
        while l <= r:
            capacity = l + (r - l) // 2
            totalDays = self.maxDays(weights, capacity)
            if totalDays > days:
                l = capacity + 1
            else:
                result = capacity
                r = capacity - 1
        return result

    
    def maxDays(self, weights, capacity):
        days = 1
        curr = 0
        for w in weights:
            if w + curr > capacity:
                days += 1
                curr = w
            else:
                curr += w
        return days