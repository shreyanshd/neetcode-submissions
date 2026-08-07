class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        maxheap = [[-count, c] for c, count in counter.items()]
        heapq.heapify(maxheap)
        
        prev = None
        result = ""
        
        while maxheap:
            count, char = heapq.heappop(maxheap)
            result += char
            count += 1
            
            if prev:
                heapq.heappush(maxheap, prev)
                prev = None
            
            if count != 0:
                prev = [count, char]

        if len(result) != len(s):
            result = ""

        return result
            