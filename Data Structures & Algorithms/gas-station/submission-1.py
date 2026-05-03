class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        
        def check(i):
            total = gas[i] - cost[i]
            for j in range(n + 1):
                nxt = (i + 1 + j) % n
                if total < 0:
                    return False
                total += (gas[nxt] - cost[nxt])
            return True
        
        for i in range(n):
            if check(i):
                return i
        
        return -1
