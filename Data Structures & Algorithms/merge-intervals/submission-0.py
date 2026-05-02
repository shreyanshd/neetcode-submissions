class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        minheap = list(intervals)
        heapq.heapify(minheap)

        result = [heapq.heappop(minheap)]
        while minheap:
            cur = result[-1]
            nxt = heapq.heappop(minheap)
            if cur[1] >= nxt[0]:
                cur[0] = min(cur[0], nxt[0])
                cur[1] = max(cur[1], nxt[1])
            else:
                result.append(nxt)
        
        return result
