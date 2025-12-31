"""
You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

 

Example 1:


Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.
Example 2:


Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: All 1s are either on the boundary or can reach the boundary.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 500
grid[i][j] is either 0 or 1.
"""

from typing import List

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # change the 1s that are on boundary
        # top row and bottom row
        for col in range(n):
            self._dfs(0, col,  grid, m, n)
            self._dfs(m-1, col, grid, m, n)
        
        # left column and right column
        for row in range(m):
            self._dfs(row, 0, grid, m, n)
            self._dfs(row, n-1, grid, m, n)

        # count the remaining ones
        enclaves_count = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    enclaves_count += 1
        
        return enclaves_count

    
    def _dfs(self, row, col, grid, m, n):
        if not(0 <= row < m and 0 <= col < n) or grid[row][col] in [0, 'T']:
            return
        
        if grid[row][col] == 1:
            grid[row][col] = 'T'

        neighbors = [(0,1), (0, -1), (1,0), (-1, 0)]
        for n_row, n_col in neighbors:
            self._dfs(row + n_row, col + n_col, grid, m, n)


input_2 = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
exected = 3
actual = Solution().numEnclaves(input_2)
print(f"expected: {exected} , actual:{actual}")

input_1 = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
exected = 0
actual = Solution().numEnclaves(input_1)
print(f"expected: {exected} , actual:{actual}")


"""
Time complexty: O(MxN)
Reason:
- dfs recursion => O(MxN) => Each cell is visited at most ones across all dfs calls. in worst case, all cells will be 1
- counting number of remaining 1s  => O(MxN)

Space Complexity: O(MxN)
Reason:
- recusrsion stack space = O(MxN) => in worst case, recursion depth = O(MxN) => snake like patterns
"""