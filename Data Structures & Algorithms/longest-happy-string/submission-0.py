class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxheap = [[-a, 'a'], [-b, 'b'], [-c, 'c']]
        heapq.heapify(maxheap)
        result = ""

        while maxheap:
            count, char = heapq.heappop(maxheap)
            if count == 0:
                continue

            if len(result) > 1 and result[-1] == result[-2] == char:
                if not maxheap:
                    break
                count2, char2 = heapq.heappop(maxheap)
                if count2 == 0:
                    continue
                result += char2
                count2 += 1
                heapq.heappush(maxheap, [count2, char2])
            else:
                result += char
                count += 1
            
            heapq.heappush(maxheap, [count, char])
        
        return result