class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        l = 0
        r = col * (row-1) + (col-1)
        while l <= r:
            m = l + (r - l) // 2
            x, y = m // col, m % col
            print("l,r", l, r)
            print("m", m)
            print("x,y", x, y)
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] < target:
                l = m + 1
            else:
                r = m - 1
        return False