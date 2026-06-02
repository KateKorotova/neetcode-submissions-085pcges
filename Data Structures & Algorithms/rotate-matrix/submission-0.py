class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix[0])
        res = list()
        for i in range(n):
            curr = []
            for j in range(n):
                curr.append(matrix[j][i])
            res.append(list(reversed(curr)))
        for i in range(n):
            for j in range(n):
                matrix[i][j] = res[i][j]
