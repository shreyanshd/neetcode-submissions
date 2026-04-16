class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # pair (temperature, idx)
        for i in range(len(temperatures) - 1, -1, -1):
            t = temperatures[i]
            while len(stack) > 0 and t >= stack[-1][0]:
                stack.pop()     
            if len(stack) == 0:
                stack.append((t, i))
                res[i] = 0
            else:
                temperature, idx = stack[-1]
                res[i] = idx - i
                stack.append((t, i))
        return res