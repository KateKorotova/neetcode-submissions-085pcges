class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
            nonlocal curr_island
            if i < 0 or j < 0 or i >= ROWS or j >= COLS or grid[i][j] == 0:
                return 
            grid[i][j] = 0
            curr_island += 1
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            for dr, dc in directions:
                dfs(i + dr, j+dc)

        ROWS = len(grid)
        COLS = len(grid[0])
        max_island = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    curr_island = 0
                    dfs(i, j)
                    max_island = max(max_island, curr_island)
        return max_island

