class Solution:
    def solve(self, grid: list[list[str]]) -> None:
        m = len(grid)
        n = len(grid[0])

        # top row and bottom row
        for col in range(n):
            self._dfs(0, col, grid, m, n)
            self._dfs(m-1, col, grid, m, n)

        # left column and right column
        for row in range(m):
            self._dfs(row, 0, grid, m, n)
            self._dfs(row, n-1, grid, m, n)
        
        # change temp back to 0 and surround remainings
        for row in range(m):
            for col in range(n):
                if grid[row][col] == "T":
                    grid[row][col] = "O"
                elif grid[row][col] == "O":
                    grid[row][col] = "X"
        
    def _dfs(self,row: int, col: int, grid: list[list[str]], m: int, n: int) -> None:
        if grid[row][col] != "O":
            return
        
        grid[row][col] = "T"
        neighbor_offset = [(0,1), (0,-1), (1,0), (-1,0)]
        for row_offset, col_offset in neighbor_offset:
            n_row = row + row_offset
            n_col = col + col_offset

            if 0 <= n_row < m and 0 <= n_col < n and grid[n_row][n_col] == "O":
                self._dfs(n_row, n_col, grid, m, n)

input_1 = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
expected_output = [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Solution().solve(input_1)
print(f"ex:{expected_output} \nac:{input_1}")

input_2 = [["X"]]
expected_output = [["X"]]
Solution().solve(input_1)
print(f"ex:{expected_output} \nac:{input_2}")
