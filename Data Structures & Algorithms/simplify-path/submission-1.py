class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        curr = ''
        for p in path + '/':
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

        result = '/'
        return result + '/'.join(stack)
