class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows_n, cols_n = len(matrix), len(matrix[0])
        lin_left = 0
        lin_right = (rows_n*cols_n) - 1

        while lin_left <= lin_right:
            mid = (lin_left + lin_right)//2
            mid_0 = mid // cols_n
            mid_1 = mid % cols_n
            matrix_mid = matrix[mid_0][mid_1]
            if matrix_mid < target:
                lin_left = mid + 1
            elif matrix_mid > target:
                lin_right = mid - 1
            else:
                return True
        return False