class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        curr = ''
        
        for p in path + '/':
            if p == '/':
                if curr == '..':
                    if stack: stack.pop()
                elif curr != '' and curr != '.':
                    stack.append(curr)
                curr = ''
            else:
                curr += p

        return '/' + '/'.join(stack)
