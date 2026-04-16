class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ('(', '[', '{'):
                stack.append(c)
            else:
                tos = stack[-1] if len(stack) > 0 else ''
                if ((c == ')' and tos == '(') or
                    (c == ']' and tos == '[') or 
                    (c == '}' and tos == '{')):
                    stack.pop()
                else:
                    return False
        return len(stack) == 0


            

