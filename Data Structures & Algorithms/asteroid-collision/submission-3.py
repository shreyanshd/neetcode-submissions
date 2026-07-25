class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        i = 0
        while i < len(asteroids):
            a = asteroids[i]
            if stack and a < 0 and stack[-1] > 0: # collision
                diff = stack[-1] + a
                if diff > 0:
                    i += 1
                elif diff < 0:
                    stack.pop()
                else:
                    stack.pop()
                    i += 1
            else:
                stack.append(a)
                i += 1

        return stack
