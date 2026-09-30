class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        ans = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    queue = deque([(r,c)])
                    grid[r][c] = '0'

                    while queue:
                        row, col = queue.popleft()
                        drs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                        for dr, dc in drs:
                            new_row = row + dr
                            new_col = col+ dc
                            if new_row < ROWS and new_row >= 0 and new_col < COLS and new_col >=0 and grid[new_row][new_col] == '1':
                                grid[new_row][new_col] = '0'
                                queue.append((new_row, new_col))
                    ans += 1
        return ans