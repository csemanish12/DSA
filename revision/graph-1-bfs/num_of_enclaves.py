from collections import deque

class Solution:
    def numEnclaves(self, grid: list[list[int]])-> int:
        m = len(grid)
        n = len(grid[0])

        # bfs traverse and mark boundary 1s as temp (-1)

        # left column and right column
        for row in range(m):
            self._bfs(row, 0, grid, m,n)
            self._bfs(row, n-1, grid, m,n)
        
        # top and bottom column
        for col in range(n):
            self._bfs(0, col, grid, m, n)
            self._bfs(m-1, col, grid, m, n)

        # count all the 1st that are still remaining
        count = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    count += 1
        
        return count
    
    def _bfs(self, node_row, node_col, grid, m, n):
        if grid[node_row][node_col] == 0:
            return
        
        neighbors = [(0, 1), (0, -1), (1,0), (-1, 0)]
        
        queue = deque()
        queue.append((node_row, node_col))
        grid[node_row][node_col] = -1

        while queue:
            node_row, node_col = queue.popleft()

            for n_row, n_col in neighbors:
                row = node_row + n_row
                col = node_col + n_col

                if (0 <= row < m and 0 <= col < n) and grid[row][col] == 1:
                    grid[row][col] = -1
                    queue.append((row, col))
        



input_2 = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
exected = 3
actual = Solution().numEnclaves(input_2)
print(f"expected: {exected} , actual:{actual}")

input_1 = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
exected = 0
actual = Solution().numEnclaves(input_1)
print(f"expected: {exected} , actual:{actual}")