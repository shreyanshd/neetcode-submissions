class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        stops = []
        for n, start, end in trips:
            stops.append([start, n])
            stops.append([end, -n])

        stops.sort()

        curr = 0
        for stop in stops:
            curr += stop[1]
            if curr > capacity:
                return False
        
        return True