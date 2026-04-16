class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        for c in s:
            if c in brackets:
                stack.append(brackets[c])
            else:
                if len(stack) == 0:
                    return False
                if stack[-1] != c:
                    return False
                stack.pop()
        
        return len(stack) == 0


            

