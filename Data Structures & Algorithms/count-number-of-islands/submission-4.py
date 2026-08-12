class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(node):
            # visited.add(node)
            i, j = node
            grid[i][j] = '0'

            if i >= 1 and grid[i-1][j] == "1" and (i-1, j):
                dfs((i-1, j))

            if i < len(grid) - 1 and grid[i+1][j] == "1":
                dfs((i+1, j))

            if j >= 1 and grid[i][j-1] == "1"  and (i, j-1) not in visited:
                dfs((i, j-1))

            if j < len(grid[0])-1 and grid[i][j+1] == "1" and (i, j+1) not in visited:
                dfs((i, j+1))
        
        visited = set()
        islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1' and (row, col) not in visited:
                    dfs((row, col))
                    islands += 1
        return islands

        
