class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2**31 - 1
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # multi-source BFS: every treasure cell starts in the queue
        queue = deque(
            (r, c) for r in range(ROWS) for c in range(COLS) if grid[r][c] == 0
        )
        distance = 1

        while queue:
            for _ in range(len(queue)):        # one layer at a time
                r, c = queue.popleft()
                for dr, dc in DIRECTIONS:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == INF:
                        grid[nr][nc] = distance   # mark on push; INF means unvisited
                        queue.append((nr, nc))
            distance += 1