class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for row in range(len(matrix)):
            l = 0
            r = len(matrix[row]) - 1
            while l <= r:
                m = l + ((r - l) // 2)
                if matrix[row][m] == target:
                    return True
                elif target < matrix[row][m]:
                    r = m-1
                else:
                    l = m+1
        return False 


