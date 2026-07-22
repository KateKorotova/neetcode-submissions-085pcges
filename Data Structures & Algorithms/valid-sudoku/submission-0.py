from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        grids = defaultdict(set)
        for row in range(len(board)):
            for col in range(len(board)):
                num = board[row][col]
                if num == '.':
                    continue
                grid = (row // 3, col // 3)
                # print(rows)
                # print(cols)
                # print(grids)
                if num in rows[row] or num in cols[col] or num in grids[grid]:
                    return False
                rows[row].add(num)
                cols[col].add(num)
                grids[grid].add(num)
        return True
