class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            grid[i][j] = '0'

            if i >= 1 and grid[i-1][j] == "1":
                dfs(i-1, j)

            if i < len(grid) - 1 and grid[i+1][j] == "1":
                dfs(i+1, j)

            if j >= 1 and grid[i][j-1] == "1":
                dfs(i, j-1)

            if j < len(grid[0])-1 and grid[i][j+1] == "1":
                dfs(i, j+1)
        
        islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    dfs(row, col)
                    islands += 1
        return islands

        
