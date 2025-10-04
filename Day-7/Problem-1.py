from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        column = len(matrix[0])
        found = False
        for i in range(row):
          for j in range(column):
            if matrix[i][j] == target:
              found = True
              break
        if (found):
           return True
        else:
           return False
sol = Solution()
print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))