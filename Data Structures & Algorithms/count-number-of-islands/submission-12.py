class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ans = 0
        visited = set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '0' or (r, c) in visited:
                    continue
                
                queue = deque([(r,c)])
                visited.add((r,c))
                while queue:
                    row, col = queue.popleft()
                    for dr, dc in DIRECTIONS:
                        nr, nc = row + dr, col+ dc
                        if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == '1' and (nr, nc) not in visited:
                            visited.add((nr, nc))
                            queue.append((nr, nc))
                ans += 1
        return ans