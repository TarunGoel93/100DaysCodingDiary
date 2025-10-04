# Matrix Diagonal Sum

from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        row = len(mat)
        column = len(mat[0])
        primary_diagonal = []
        for i in range(row):
            for j in range(column):
                if i == j:
                    primary_diagonal.append(mat[i][j])

        secondary_diagonal = []
        for i in range(row):
            for j in range(column):
                if i+j==row-1:
                    secondary_diagonal.append(mat[i][j])


        if row%2==1:
            mid = row//2
            ce = mat[mid][mid]
        else:
            ce = 0

        sum1 = 0
        for i in range(len(primary_diagonal)):
            sum1+=primary_diagonal[i]

        sum2 = 0
        for i in range(len(secondary_diagonal)):
            sum2+=secondary_diagonal[i]
 

        final_sum = sum1+sum2-ce
        return (final_sum)
        