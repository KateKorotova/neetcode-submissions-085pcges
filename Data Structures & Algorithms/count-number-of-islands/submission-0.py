class Solution:
    def dfs(self, start, grid, islands=[]):
        i = start[0]
        j = start[1]
        if grid[i][j] == "1":
            grid[i][j] = "-1"
            islands.append((i,j))
            if j > 0:
                start = [i, j-1]
                self.dfs(start, grid, islands)
            if j < (len(grid[0]) - 1):
                start = [i, j+1]
                self.dfs(start, grid, islands)
            if i > 0:
                start = [i - 1, j]
                self.dfs(start, grid, islands)
            if i < (len(grid) - 1):
                start = [i + 1, j]
                self.dfs(start, grid, islands)
        return grid
        

    def numIslands(self, grid: List[List[str]]) -> int:
        islands = []
        num_island = 0
        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    grid = self.dfs([i, j], grid, islands)
                    if len(islands) > 0:
                        num_island+=1
                        islands = []
        return num_island
                    

        