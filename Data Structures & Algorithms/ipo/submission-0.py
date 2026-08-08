class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = [[c, p] for c, p in zip(capital, profits)]
        queue = deque(sorted(projects))
        maxheap = []
        
        while k > 0:
            while queue and queue[0][0] <= w:
                c, p = queue.popleft()
                heapq.heappush(maxheap, -p)
            
            if maxheap:
                p = -heapq.heappop(maxheap)
                w += p
                k -= 1
            else:
                break

        return w 