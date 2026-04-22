class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(curr, opn, close):
            if opn == n and close == n:
                result.append(curr)
                return
            
            if opn < n:
                backtrack(curr + "(", opn + 1, close)
            if close < opn:
                backtrack(curr + ")", opn, close + 1)
        
        backtrack("", 0, 0)
        return result