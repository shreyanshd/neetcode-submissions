class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        visited = set()

        def backtrack(i, j, k):
            if k == len(word):
                return True
            if i < 0 or j < 0 or i >= row or j >= col:
                return False
            if (i,j) in visited:
                return False
            if board[i][j] != word[k]:
                return False
            visited.add((i, j))
            result = (
                backtrack(i + 1, j, k + 1) or
                backtrack(i, j + 1, k + 1) or
                backtrack(i - 1, j, k + 1) or
                backtrack(i, j - 1, k + 1)
            )
            visited.remove((i, j))
            return result
        
        
        for i in range(row):
            for j in range(col):
                if backtrack(i, j, 0):
                    return True
        
        return False