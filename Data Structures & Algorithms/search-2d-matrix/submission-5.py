class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        lo = 0
        hi = row * col - 1
        
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            r = mid // col
            c = mid % col
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                hi = mid - 1
            else:
                lo = mid + 1

        return False 