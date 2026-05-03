class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if groupSize == 1:
            return True
        if len(hand) < groupSize:
            return False
        
        counter = defaultdict(int)
        for h in hand:
            counter[h] += 1
        
        while counter:
            start = min(counter.keys())
            end = start + groupSize
            for i in range(start, end):
                if i not in counter:
                    return False
                else:
                    counter[i] -= 1
                    if counter[i] == 0:
                        del counter[i]
        return True

        

