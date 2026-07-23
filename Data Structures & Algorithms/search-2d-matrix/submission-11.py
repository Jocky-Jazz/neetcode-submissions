class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0])
        l, r, mid = 0, len(matrix)*n-1, 0
        while (l <= r):
            mid = l + ((r-l)>>1)
            i = mid//n
            j = mid%n
            if (matrix[i][j]==target):
                return True
            elif (matrix[i][j]<target):
                l = mid+1
            else:
                r = mid-1
        return False
