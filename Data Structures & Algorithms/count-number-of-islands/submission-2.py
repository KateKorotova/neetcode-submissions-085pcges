class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(node, grid, visited):
            visited.add(node)
            i, j = node
            if i >= 1 and grid[i-1][j] == "1" and (i-1, j) not in visited:
                dfs((i-1, j),grid, visited)
            if i < len(grid) - 1 and grid[i+1][j] == "1" and  (i+1, j) not in visited:
                dfs((i+1, j), grid, visited)
            if j >= 1 and grid[i][j-1] == "1"  and (i, j-1) not in visited:
                dfs((i, j-1),grid, visited)
            if j < len(grid[0])-1 and grid[i][j+1] == "1" and (i, j+1) not in visited:
                dfs((i, j+1),grid, visited)
        
        visited = set()
        islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1' and (row, col) not in visited:
                    dfs((row, col), grid, visited)
                    islands += 1
        return islands

        
