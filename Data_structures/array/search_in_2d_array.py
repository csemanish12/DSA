"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.



Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""


class Solution:
    """
    rows of matrix are sorted, so if we flatten them, they will become 1D sorted matrix and
    thus binary search can be used.
    to get row and column:,
    row = mid //column_size
    column = mid % column_size
    """

    def searchMatrix(self, matrix, target):
        n = len(matrix)
        m = len(matrix[0])

        # apply binary search:
        low = 0
        high = n * m - 1
        while low <= high:
            mid = (low + high) // 2
            row = mid // m
            col = mid % m
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False


s = Solution()
input_1 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target_1 = 5
print("target found:", s.searchMatrix(input_1, target_1))

input_2 = [[1]]
target_2 = 1
print("target found:", s.searchMatrix(input_2, target_2))

input_3 = [[1, 1]]
target_3 = 3
print("target found:", s.searchMatrix(input_3, target_3))
