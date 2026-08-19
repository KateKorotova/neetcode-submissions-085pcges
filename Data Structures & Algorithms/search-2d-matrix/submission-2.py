class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nrow, ncol = len(matrix), len(matrix[0])
        l, r = 0, nrow*ncol - 1
        while l <= r:
            mid = l + ((r-l)//2)
            mid_row = mid // ncol
            mid_col = mid % ncol
            if matrix[mid_row][mid_col] < target:
                l = mid + 1
            elif matrix[mid_row][mid_col] > target:
                r = mid - 1
            else:
                return True
        return False


