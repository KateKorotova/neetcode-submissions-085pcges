class Solution:
    def dfs(self, start, grid):
        i = start[0]
        j = start[1]
        if grid[i][j] == "1":
            grid[i][j] = "-1"
            if j > 0:
                start = [i, j-1]
                self.dfs(start, grid)
            if j < (len(grid[0]) - 1):
                start = [i, j+1]
                self.dfs(start, grid)
            if i > 0:
                start = [i - 1, j]
                self.dfs(start, grid)
            if i < (len(grid) - 1):
                start = [i + 1, j]
                self.dfs(start, grid)
        return grid
        

    def numIslands(self, grid: List[List[str]]) -> int:
        num_island = 0
        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    grid = self.dfs([i, j], grid)
                    num_island+=1
        return num_island
                    

        