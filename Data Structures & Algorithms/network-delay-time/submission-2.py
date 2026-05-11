class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for u, v, t in times:
            edges[u].append((v, t))
        
        minHeap = [(0, k)]
        visited = set()
        t = 0

        while minHeap:
            t1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)
            t = max(t, t1)

            for n2, t2, in edges[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, (t1 + t2, n2))

        return t if len(visited) == n else -1