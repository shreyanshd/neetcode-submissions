class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        points = [0] * 1001
        for p, start, end in trips:
            points[start] += p
            points[end] -= p
        
        current = 0
        for p in points:
            current += p
            if current > capacity:
                return False
        
        return True