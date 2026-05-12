class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visit = set()
        minHeap = [(grid[0][0], 0, 0)]
        visit.add((0, 0))
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            
            if r == n - 1 and c == n - 1:
                return t

            for dr, dc in directions:
                p = r + dr
                q = c + dc
                if (p < 0 or q < 0 or p == n or q == n or
                   (p, q) in visit):
                   continue
                visit.add((p, q))
                time = max(t, grid[p][q])
                heapq.heappush(minHeap, (time, p, q))
            