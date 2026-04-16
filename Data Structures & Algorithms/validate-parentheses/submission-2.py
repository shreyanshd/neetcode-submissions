class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matchingBraces = {
            ')' : '(',
            ']' : '[',
            '}' : '{',
        }
        for c in s:
            if c in matchingBraces:
                tos = stack[-1] if len(stack) > 0 else ''
                if tos == matchingBraces[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0


            

