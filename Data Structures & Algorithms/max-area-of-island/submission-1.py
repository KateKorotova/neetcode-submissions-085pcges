class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
            if i < 0 or j < 0 or i >= ROWS or j >= COLS or grid[i][j] == 0:
                return 0
            grid[i][j] = 0

            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            res = 1
            for dr, dc in directions:
                res += dfs(i + dr, j+dc)
            return res

        ROWS = len(grid)
        COLS = len(grid[0])
        max_island = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    max_island = max(max_island, dfs(i, j))
        return max_island

