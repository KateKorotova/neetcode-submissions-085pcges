class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        nROWS = len(grid)
        nCOLS = len(grid[0])
        
        def dfs(i, j):
            if i < 0 or i >= nROWS or j < 0 or j >= nCOLS or grid[i][j] == 0:
                return 0 
            grid[i][j] = 0
            return 1 + dfs(i + 1, j) + dfs(i, j + 1) + dfs(i - 1, j) + dfs(i, j - 1)

        maxArea = 0
        for row in range(nROWS):
            for col in range(nCOLS):
                if grid[row][col] == 1:
                    area = dfs(row, col)
                    maxArea = max(maxArea, area)
        return maxArea
