class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if groupSize == 1:
            return True
        if len(hand) % groupSize != 0:
            return False
        
        freq = defaultdict(int)
        for h in hand:
            freq[h] += 1

        minHeap = list(hand)
        heapq.heapify(minHeap)
        
        while minHeap:
            minVal = heapq.heappop(minHeap)
            if freq[minVal] == 0:
                continue

            for i in range(minVal, minVal + groupSize):
                if freq[i] == 0:
                    return False
                freq[i] -= 1

        return True

        

