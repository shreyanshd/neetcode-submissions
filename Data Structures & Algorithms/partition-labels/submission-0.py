class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        result = []

        def partition(p):
            if not p or len(p) == 0:
                return

            maxIndex = {}
            for i, c in enumerate(p):
                maxIndex[c] = i

            rightmost = 0
            for i, c in enumerate(p):
                rightmost = max(rightmost, maxIndex[c])
                if rightmost == i:
                    result.append(rightmost + 1)
                    return partition(p[rightmost+1:])
            
            result.append(len(p))
            return
        
        partition(s)
        return result

            