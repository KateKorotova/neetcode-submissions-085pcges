class Solution:
    def solve(self, board: List[List[str]]) -> None:
        nROWS, nCOLS = len(board), len(board[0])
        DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        queue_seed = set()
        queue_seed.update([(0, i) for i in range(nCOLS) if board[0][i] == "O"])
        queue_seed.update([(i, 0) for i in range(nROWS) if board[i][0] == "O"])
        queue_seed.update([(nROWS-1, i) for i in range(nCOLS) if board[nROWS-1][i] == "O"])
        queue_seed.update([(i, nCOLS-1) for i in range(nROWS) if board[i][nCOLS-1] == "O"])

        not_surr = set(queue_seed)
        queue = deque(queue_seed)
        while queue:
            row, col = queue.popleft()
            for dr, dc in DIRECTIONS:
                nr, nc = row+dr, col+dc
                if 0<= nr < nROWS and 0 <= nc < nCOLS and board[nr][nc] == 'O' and (nr, nc) not in not_surr:
                    not_surr.add((nr, nc))
                    queue.append((nr, nc))

        for row in range(nROWS):
            for col in range(nCOLS):
                if board[row][col] == 'O' and (row, col) not in not_surr:
                    board[row][col] = 'X'
        
