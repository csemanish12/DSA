"""
Problem Statement: Given a matrix if an element in the matrix is 0 then you will have to set its entire column
and row to 0 and then return the matrix.

Examples 1:

Input: matrix=[[1,1,1],[1,0,1],[1,1,1]]

Output: [[1,0,1],[0,0,0],[1,0,1]]

Explanation: Since matrix[2][2]=0.Therfore the 2nd column and 2nd row wil be set to 0.

Input: matrix=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]

Output:[[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Explanation:Since matrix[0][0]=0 and matrix[0][3]=0. Therefore 1st row, 1st column and 4th column will be set to 0
"""
from typing import List


class Solution:
    """
    Approach: 1
    Traverse the matrix and find the index of elements whose value is zero.
    Traverse the indexes obtained and set the value for row and column to zero.
    For row, increase the x coordinate
    for column, increase the y coordinate
    """
    def set_zeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        indices = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    indices.append((i, j))
        for each_index in indices:
            # traversing row
            for i in range(len(matrix)):
                matrix[i][each_index[1]] = 0

            # traversing column
            for j in range(len(matrix[0])):
                matrix[each_index[0]][j] = 0


example_1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
example_2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]

solution = Solution()

solution.set_zeroes(example_1)
print("example 1 output:", example_1)

solution.set_zeroes(example_2)
print("example 2 output", example_2)