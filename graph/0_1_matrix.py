"""
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two cells sharing a common edge is 1.

 

Example 1:


Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
Example 2:


Input: mat = 
[[0,0,0],
[0,1,0],
[1,1,1]]
Output: 
[[0,0,0],
[0,1,0],
[1,2,1]]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.

"""
from typing import List
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        updated_matrix = [[-1 for _ in range(n)] for _ in range(m)]
        visited = [[False for _ in range(n)] for _ in range(m)]
        queue = deque()

        # iterate over each element in matrix
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 0:
                    queue.append((row, col, 0))
                    visited[row][col] = True

        neighbors = [(0,-1), (0, 1), (-1, 0), (1,0)]

        while queue:
            curr_row, curr_col, curr_distance = queue.popleft()
            updated_matrix[curr_row][curr_col] = curr_distance

            for n_row, n_col in neighbors:
                row = curr_row + n_row
                col = curr_col + n_col

                if (0 <= row < m and 0 <= col < n) and not visited[row][col]:
                    queue.append((row, col, curr_distance + 1))
                    visited[row][col] = True
                    
        return updated_matrix
    

        
    


# input_1 = [[0,0,0],[0,1,0],[1,1,1]]
# expected_output =[[0,0,0],[0,1,0],[1,2,1]]
# actual_output = Solution().updateMatrix(input_1)
# print(f"expected:{expected_output}, actual_output:{actual_output}")
# print(f"expected == actula?", expected_output == actual_output)

input_1 = [[1,1,1],[1,1,1],[1,1,0]]
expected_output =[[4,3,2],[3,2,1],[2,1,0]]
actual_output = Solution().updateMatrix(input_1)
print(f"expected:{expected_output}, actual_output:{actual_output}")
print(f"expected == actula?", expected_output == actual_output)        



"""
Time complexity: O(MxN)
- finding cells that has zero => O(MxN)
- bfs on all zeroes => O(MxN) => worst case all cells are zeroes
Hence, O(MxN) + O(MxN) => O(MxN)

Space complexity: O(MxN)
- matrix to store distance => O(MxN)
- visited array  => O(MxN)
- queue => O(min(M,N)) => BFS level width
Hence, O(MxN) + O(MxN) + O(min(M,N)) => O(MxN)
"""