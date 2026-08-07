class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter()
        for c in s:
            counter[c] += 1

        maxheap = [[-count, c] for c, count in counter.items()]
        heapq.heapify(maxheap)
        prev_char = ''
        prev_count = 0
        result = ''
        
        while maxheap:
            count, c = heapq.heappop(maxheap)
            result += c
            
            if prev_count < 0:
                heapq.heappush(maxheap, [prev_count, prev_char])
            
            count += 1
            prev_char = c
            prev_count = count

        if len(result) != len(s):
            result = ""

        return result
            