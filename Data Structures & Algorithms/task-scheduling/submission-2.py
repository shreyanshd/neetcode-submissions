class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        minHeap = [[0, c] for c in counter.values()]
        heapq.heapify(minHeap)
        time = 0

        while minHeap:
            t = minHeap[0][0]
            if t <= time:
                t, count = heapq.heappop(minHeap)
                count -= 1
                if count > 0:
                    next_time = t + n + 1
                    heapq.heappush(minHeap, [next_time, count])
                time += 1
            else:
                time = t
        
        return time