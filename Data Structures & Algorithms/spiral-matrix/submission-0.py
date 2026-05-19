class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        left = 0
        bottom = len(matrix) - 1
        right = len(matrix[0]) - 1

        result = []
        
        while left <= right and top <= bottom:
            if top <= bottom:
                # left to right
                for i in range(left, right + 1):
                    result.append(matrix[top][i])
                top = top + 1

            if left <= right:
                # top to bottom
                for j in range(top, bottom + 1):
                    result.append(matrix[j][right])
                right = right - 1

            if top <= bottom:
                # right to left
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom = bottom - 1

            if left <= right:
                # bottom to top
                for j in range(bottom, top - 1, -1):
                    result.append(matrix[j][left])
                left = left + 1

        return result