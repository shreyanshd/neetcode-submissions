class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = [[c, p] for c, p in zip(capital, profits)]
        queue = deque(sorted(projects))
        maxheap = []

        while k > 0:
            while queue and queue[0][0] <= w:
                c, profit = queue.popleft()
                heapq.heappush(maxheap, -profit)
            
            if maxheap:
                profit = -heapq.heappop(maxheap)
                w += profit
                k -= 1
            else:
                break

        return w