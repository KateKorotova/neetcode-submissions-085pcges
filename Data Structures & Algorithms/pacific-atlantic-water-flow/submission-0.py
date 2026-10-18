class Solution:

        

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        nROWS, nCOLS = len(heights), len(heights[0])
        DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        queue_pac = deque([])
        queue_pac.extend([[0, i] for i in range(nCOLS)])
        queue_pac.extend([[i, 0] for i in range(nROWS) if [i, 0] not in queue_pac])

        queue_atl= deque([])
        queue_atl.extend([[nROWS-1, i] for i in range(nCOLS)])
        queue_atl.extend([[i, nCOLS-1] for i in range(nROWS) if [i, nCOLS-1] not in queue_atl])


        def bfs(queue, visited):
            while queue:
                row, col = queue.pop()
                height = heights[row][col]
                for dr, dc in DIRECTIONS:
                    nr, nc = row+dr, col+dc
                    if 0 <= nr < nROWS and 0 <= nc < nCOLS and heights[nr][nc] >= height and [nr, nc] not in visited:
                        visited.append([nr, nc])
                        queue.append([nr, nc])
        
        pacific_cells = queue_pac.copy()
        bfs(queue_pac, pacific_cells)

        atlantic_cells = queue_atl.copy()
        bfs(queue_atl, atlantic_cells)


        return [x for x in pacific_cells if x in atlantic_cells]


