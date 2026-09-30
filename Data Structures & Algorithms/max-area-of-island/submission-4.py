class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            if r >= ROWS or r < 0 or c >= COLS or c < 0 or grid[r][c] == 0:
                return 0 
            grid[r][c] = 0
            drs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            cur = 1
            for dr, dc in drs:
                cur += dfs(r+dr, c+dc)
            return cur
        
        ROWS = len(grid)
        COLS = len(grid[0])
        ans = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = dfs(r,c)
                    ans = max(ans, area)
        return ans 