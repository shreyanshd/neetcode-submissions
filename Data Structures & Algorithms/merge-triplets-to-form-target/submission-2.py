class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        result = []
        for t in triplets:
            valid = True
            for j in range(3):
                if t[j] > target[j]:
                    valid = False
                    break
            if valid:
                result.append(t)
        
        final = [float('-inf') for _ in range(3)]
        for r in result:
            for j in range(3):
                final[j] = max(final[j], r[j])
        
        return final == target

                    
