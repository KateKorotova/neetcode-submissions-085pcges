class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        rotten = [(r, c) for r in range(ROWS) for c in range(COLS) if grid[r][c] == 2]
        if not rotten:
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 1:
                        return -1
            return 0

        time = 0
        queue = deque(rotten)

        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for dr, dc in DIRECTIONS:
                    nr, nc = row+dr, col+dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
            time += 1


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        return time-1

        