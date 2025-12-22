"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
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
    def orangesRotting(self, grid: list[list[int]]) -> int:
        total_oranges = 0
        rotten_oranges = 0
        queue = deque()
        m = len(grid)
        n = len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        time_taken = 0

        # get initial rotten oranges
        for row in range(m):
            for column in range(n):
                if grid[row][column] == 1:
                    total_oranges += 1
                elif grid[row][column] == 2:
                    rotten_oranges += 1
                    total_oranges += 1
                    queue.append((row, column, time_taken))
                    visited[row][column] = True

        # Check if there is any fresh orange
        if rotten_oranges == total_oranges:
            return time_taken

        # traverse the grid
        while queue:
            row, column, current_time_taken = queue.popleft()
            neighbors = self._get_neighbors(row, column, m, n)
            print(f"node= {(row, column)} neighbor:{neighbors}")
            if not neighbors:
                continue
            
            for neighbor_row, neighbor_col in neighbors:
                if not visited[neighbor_row][neighbor_col] and grid[neighbor_row][neighbor_col] == 1:
                    queue.append((neighbor_row, neighbor_col, current_time_taken + 1))
                    visited[neighbor_row][neighbor_col] = True
                    rotten_oranges += 1
            
        time_taken = max(time_taken, current_time_taken)


        if total_oranges != rotten_oranges:
            return -1

        return time_taken



    
    def _get_neighbors(self, row: int, column: int, row_size: int, col_size: int):
        neighbors = []

        # up neighbor
        if row - 1 >= 0:
            neighbors.append((row - 1, column))

        # down
        if row + 1 < row_size:
            neighbors.append((row + 1, column))

        # left
        if column - 1 >= 0:
            neighbors.append((row, column - 1))
        
        # right
        if column + 1 < col_size:
            neighbors.append((row, column + 1))
        
        return neighbors
    


"""
Space complexity: O(mxn)
- visited array = O(mxn)
- queue = O(mxn) => worst case, when all the oranges are  rotten

Time complexity: O(mxn)
- get initial rotten oranges = O(mxn)
- bfs traversal O(V)

"""