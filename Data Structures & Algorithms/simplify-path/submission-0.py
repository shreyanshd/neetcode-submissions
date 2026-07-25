class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        curr = ''
        for p in path:
            if p == '/':
                if curr == '.' or curr == '':
                    curr = ''
                elif curr == '..':
                    if stack:
                        stack.pop()
                    curr = ''
                else:
                    stack.append(curr)
                    curr = ''
            else:
                curr += p
        
        if len(curr) > 0:
            if curr == '.':
                pass
            elif curr == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(curr)

        result = '/'
        return result + '/'.join(stack)
