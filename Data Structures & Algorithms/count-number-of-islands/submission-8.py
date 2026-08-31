class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nROWS = len(grid)
        nCOLS = len(grid[0])
        def dfs(i, j):
            if i < 0 or i >= nROWS or j < 0 or j >= nCOLS or grid[i][j] == "0":
                return 
            grid[i][j] = '0'
            drc = [[0, 1], [1, 0], [-1, 0], [0, -1]]
            for row, col in drc:
                dfs(i + row, j + col)
        res = 0
        for row in range(nROWS):
            for col in range(nCOLS):
                if grid[row][col] == '1':
                    dfs(row, col)
                    res += 1
        return res

            