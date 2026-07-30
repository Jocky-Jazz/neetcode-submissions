class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                if (i < j):
                    matrix[i][j] ^= matrix[j][i]
                    matrix[j][i] ^= matrix[i][j]
                    matrix[i][j] ^= matrix[j][i]
        for i in range(n):
            matrix[i].reverse()