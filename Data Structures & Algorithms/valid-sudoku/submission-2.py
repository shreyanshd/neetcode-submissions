class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                b = board[r][c]
                if b == ".": continue
                if (b in cols[c] or
                    b in rows[r] or
                    b in squares[(r//3, c//3)]):
                    return False
                rows[r].add(b)
                cols[c].add(b)
                squares[(r//3, c//3)].add(b)
        
        return True