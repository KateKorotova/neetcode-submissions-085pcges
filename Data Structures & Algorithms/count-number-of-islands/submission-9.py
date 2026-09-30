class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r, c):
            if r >= ROWS or r < 0 or c >= COLS or c < 0 or grid[r][c] == '0':
                return 
            grid[r][c] = '0'
            drs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for dr, dc in drs:
                dfs(r+dr, c+dc)
            
        ROWS = len(grid)
        COLS = len(grid[0])
        ans = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    dfs(r,c)
                    ans += 1
        return ans
