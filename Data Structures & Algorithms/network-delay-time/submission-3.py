class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for u, v, t in times:
            edges[u].append((v, t))
        
        minHeap = [(0, k)]
        visited = set()
        t = 0

        while minHeap:
            t1, u = heapq.heappop(minHeap)
            if u in visited:
                continue
            visited.add(u)
            t = max(t, t1)

            for v, t2, in edges[u]:
                if v not in visited:
                    heapq.heappush(minHeap, (t1 + t2, v))

        return t if len(visited) == n else -1