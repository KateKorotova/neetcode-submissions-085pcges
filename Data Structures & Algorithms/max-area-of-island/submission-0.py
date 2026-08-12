class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
            if i < 0 or j < 0 or i >= ROWS or j >= COLS or grid[i][j] == 0:
                return 0 
            grid[i][j] = 0
            return (1 + dfs(i + 1, j) + 
                        dfs(i - 1, j) + 
                        dfs(i, j - 1) + 
                        dfs(i, j + 1)
            )

        ROWS = len(grid)
        COLS = len(grid[0])
        max_island = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    curr_island = dfs(i, j)
                    max_island = max(max_island, curr_island)
        return max_island

