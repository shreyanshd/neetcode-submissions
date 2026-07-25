class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for c in s:
            if c != ']':
                stack.append(c)
            else:
                # 1. Get the substring
                substr = ''
                while stack[-1] != '[':
                    substr = stack.pop() + substr
                
                # 2. Pop '['
                stack.pop()

                # 3. Get the digits (k)
                k = ''
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                
                # 4. Add result back to stack
                result = int(k) * substr
                stack.append(result)
        
        return ''.join(stack)