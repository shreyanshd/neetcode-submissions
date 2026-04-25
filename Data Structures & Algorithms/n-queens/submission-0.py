class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []

        def backtrack(queen, row, curr):
            if queen == n:
                solution = []
                for x in range(n):
                    s = ""
                    for y in range(n):
                        if (x,y) in curr:
                            s += "Q"
                        else:
                            s += "."
                    solution.append(s)
                result.append(solution)
                return
            
            for col in range(n):
                if isValid(row, col, n, curr):
                    curr.add((row, col))
                    backtrack(queen + 1, row + 1, curr)
                    curr.remove((row, col))

            
        def isValid(i, j, n, points):
            for x,y in points:
                if i == x: return False
                if j == y: return False
            
            x, y = i, j
            while x >= 0 and y >= 0:
                if (x,y) in points:
                    return False
                x, y = x-1, y-1
            
            x, y = i, j
            while x >= 0 and y < n:
                if (x,y) in points:
                    return False
                x, y = x-1, y+1

            x, y = i, j
            while x < n and y >= 0:
                if (x,y) in points:
                    return False
                x, y = x+1, y-1

            x, y = i, j
            while x < n and y < n:
                if (x,y) in points:
                    return False
                x, y = x+1, y+1

            return True

        curr = set()
        backtrack(0, 0, curr)
        return result