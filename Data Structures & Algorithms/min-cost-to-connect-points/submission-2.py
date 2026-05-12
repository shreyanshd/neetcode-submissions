class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((dist, j))
                adj[j].append((dist, i))
        
        minHeap = [(0, 0)]
        visit = set()
        cost = 0

        while minHeap and len(visit) < len(points):
            dist, p = heapq.heappop(minHeap)
            if p in visit:
                continue
            visit.add(p)
            cost += dist
            for d, q in adj[p]:
                heapq.heappush(minHeap, (d, q))

        return cost


        
