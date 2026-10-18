class Solution:

        

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        nROWS, nCOLS = len(heights), len(heights[0])
        DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        queue_pacific = set()
        queue_pacific.update([(0, i) for i in range(nCOLS)])
        queue_pacific.update([(i, 0) for i in range(nROWS)])

        queue_atlantic= set()
        queue_atlantic.update([(nROWS-1, i) for i in range(nCOLS)])
        queue_atlantic.update([(i, nCOLS-1) for i in range(nROWS)])


        def bfs(queue, visited):
            while queue:
                row, col = queue.popleft()
                height = heights[row][col]
                for dr, dc in DIRECTIONS:
                    nr, nc = row+dr, col+dc
                    if 0 <= nr < nROWS and 0 <= nc < nCOLS and heights[nr][nc] >= height and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
        
        pacific_cells = set(queue_pacific)
        bfs(deque(queue_pacific), pacific_cells)

        atlantic_cells = set(queue_atlantic)
        bfs(deque(queue_atlantic), atlantic_cells)

        ans = [[r, c] for r, c in pacific_cells.intersection(atlantic_cells)]
        
        return ans


