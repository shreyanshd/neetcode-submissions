class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        output = [0] * n
        stack = [] # (index, temp) | monotonically decreasing stack

        for i in range(n - 1, -1, -1):
            temperature = temperatures[i]
            while len(stack) > 0 and stack[-1][1] <= temperature:
                stack.pop()
            if stack:
                output[i] = stack[-1][0] - i
            stack.append((i, temperature))

        return output