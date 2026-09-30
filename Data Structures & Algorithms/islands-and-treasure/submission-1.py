class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        treasure = []
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    treasure.append((r,c))
        queue = deque([treasure])

        distance = 1
        while queue:
            nodes = queue.popleft()
            new_nodes = set()
            for r, c in list(nodes):
                for dr, dc in DIRECTIONS:
                    nr, nc = r+dr, c+dc
                    if 0<= nr < ROWS and 0<= nc < COLS and grid[nr][nc] == (2**31 - 1):
                        grid[nr][nc] = distance
                        new_nodes.add((nr, nc))
            if len(new_nodes) > 0:
                queue.append(new_nodes)

            distance += 1

        