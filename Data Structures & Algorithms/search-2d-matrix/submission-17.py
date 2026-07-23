class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r, row = 0, len(matrix)-1, 0
        while (l <= r):
            row = l + ((r-l)>>1)
            if (matrix[row][-1]<target):
                l = row+1
            elif (matrix[row][0]>target):
                r = row-1
            else:
                break
        l, r = 0, len(matrix[0])-1
        while (l <= r):
            mid = l + ((r-l)>>1)
            if (matrix[row][mid]==target):
                return True
            elif (matrix[row][mid]<target):
                l = mid+1
            elif (matrix[row][mid]>target):
                r = mid-1
        return False
            
        
