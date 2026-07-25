class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        i = 0
        while i < len(asteroids):
            a = asteroids[i]
            if not stack or a > 0 or a < 0 and stack[-1] < 0:
                stack.append(a)
                i += 1
            else:
                if abs(a) > abs(stack[-1]):
                    stack.pop()
                elif abs(a) < abs(stack[-1]):
                    i += 1
                else:
                    stack.pop()
                    i += 1
        return stack
