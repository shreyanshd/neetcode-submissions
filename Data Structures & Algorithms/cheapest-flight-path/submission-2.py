class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for s, d, p in flights:
            adj[s].append((d, p))

        minHeap = [(0, -1, src)] #(price, stops, node)
        while minHeap:
            price, stops, node = heapq.heappop(minHeap)
            if node == dst:
                return price
            
            if stops < k:
                for d, p in adj[node]:
                    heapq.heappush(minHeap, (price + p, stops + 1, d))

        return -1