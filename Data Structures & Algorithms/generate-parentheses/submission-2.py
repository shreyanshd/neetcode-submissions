class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        curr = []

        def dfs(open_count, close_count):
            if open_count == close_count == n:
                s = "".join(curr)
                result.append(s)
                return
            
            if open_count < n:
                curr.append('(')
                dfs(open_count + 1, close_count)
                curr.pop()

            if close_count < open_count:
                curr.append(')')
                dfs(open_count, close_count + 1)
                curr.pop()
        
        dfs(0, 0)
        return result