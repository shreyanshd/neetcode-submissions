class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        queue = []
        for i, task in enumerate(tasks):
            queue.append([task[0], task[1], i])
        
        queue = deque(sorted(queue))
        minheap = []
        t = 0
        order = []

        print(queue)

        while minheap or queue:
            while queue and queue[0][0] <= t:
                e, p, idx = queue.popleft()
                heapq.heappush(minheap, [p, idx])
            
            if minheap:
                p, idx = heapq.heappop(minheap)
                t += p
                order.append(idx)
            else:
                t = queue[0][0]

        return order