from collections import deque

class Solution:
    def solve(self, grid: list[list[int]])-> list[list[int]]:
        m = len(grid)
        n = len(grid[0])

        # traverse from boundary cells and mark Os as temp

        # left col and right col
        for row in range(m):
            self._bfs(row, 0, grid)
            self._bfs(row, n-1, grid)

        # top row and bottom row
        for col in range(n):
            self._bfs(row, col, grid)
            self._bfs(m-1, col, grid)
        
        # mark all remaining cells as x and reverese temp to 0 
        for row in range(m):
            for col in range(n):
                if grid[row][col] == "O":
                    grid[row][col] = "X"
                
                elif grid[row][col] == "T":
                    grid[row][col] = "O"
        
        return grid


    def _bfs(self, node_row, node_col, grid):
        if grid[node_row][node_col] == "X":
            return
        
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        queue.append((node_row, node_col))
        neighbors = [(1,0), (-1, 0), (0, 1), (0,-1)]
        grid[node_row][node_col] = "T"

        while queue:
            node_row, node_col = queue.popleft()
            
            for n_row, n_col in neighbors:
                row = node_row + n_row
                col = node_col + n_col

                if (0 <= row < m and 0 <= col < n) and grid[row][col] == "O":
                    queue.append((row, col))
                    grid[row][col] = "T"
        





input_1 = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
expected_output = [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Solution().solve(input_1)
print(f"ex:{expected_output} \nac:{input_1}")

input_2 = [["X"]]
expected_output = [["X"]]
Solution().solve(input_1)
print(f"ex:{expected_output} \nac:{input_2}")
