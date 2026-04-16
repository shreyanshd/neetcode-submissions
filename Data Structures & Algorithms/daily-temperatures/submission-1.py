class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []
        for i in range(n-1, -1, -1):
            currTemperature = temperatures[i]
            while len(stack) > 0 and currTemperature >= stack[-1][0]:
                stack.pop()
            
            if len(stack) == 0:
                stack.append((currTemperature, i))
                res[i] = 0
            else:
                temperature, idx = stack[-1]
                res[i] = idx - i
                stack.append((currTemperature, i))
        return res