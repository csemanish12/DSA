"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

Example 1:


Input: grid = [
[2,1,1],
[1,1,0],
[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
"""
from collections import deque

class Solution:
    def rotten_oranges(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        visited = [[False for _ in range(n)] for _ in range(m)]
        queue = deque()
        oranges_to_rot = 0
        minutes_required = 0

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2:
                    queue.append((row, col, 0))
                    visited[row][col] = True
                elif grid[row][col] == 1:
                    oranges_to_rot += 1
        
        if oranges_to_rot == 0:
            return 0
        
        
        neightbors = [(1,0), (-1, 0), (0,1), (0,-1)]

        while queue:
            rotten_row, rotten_col, time_taken = queue.popleft()

            for n_row, n_col in neightbors:
                row = rotten_row + n_row
                col = rotten_col + n_col

                if (0 <= row < m and 0 <= col < n) and not visited[row][col] and grid[row][col] == 1:
                    queue.append((row, col, time_taken + 1))
                    visited[row][col] = True
                    grid[row][col] = 2
                    oranges_to_rot -= 1
            
            minutes_required = max(time_taken, minutes_required)
        
        if oranges_to_rot == 0:
            return minutes_required
        
        return -1 
            

input_1 = [[2,1,1],[1,1,0],[0,1,1]]
expected_output = 4
actual_output = Solution().rotten_oranges(input_1)
print(f"expected:{expected_output}, actual_output:{actual_output}")

input_1 = [[2,1,1],[0,1,1],[1,0,1]]
expected_output = -1
actual_output = Solution().rotten_oranges(input_1)
print(f"expected:{expected_output}, actual_output:{actual_output}")

input_1 = [[0,2]]
expected_output = 0
actual_output = Solution().rotten_oranges(input_1)
print(f"expected:{expected_output}, actual_output:{actual_output}")