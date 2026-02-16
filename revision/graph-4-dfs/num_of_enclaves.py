class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # top and bottom row
        for col in range(n):
            self._dfs(0, col, grid, m, n)
            self._dfs(m-1, col, grid, m, n)
        
        # left and right col
        for row in range(m):
            self._dfs(row, 0, grid, m, n)
            self._dfs(row, n-1, grid, m, n)
        
        num_of_enclaves = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    num_of_enclaves += 1
        
        return num_of_enclaves
    
    def _dfs(self, row: int, col: int, grid: list[list[int]], m: int, n: int) -> None:
        if grid[row][col] != 1:
            return
        
        grid[row][col] = 2

        neighbor_offset = [(1,0), (-1,0), (0,1), (0,-1)]
        for row_offset, col_offset in neighbor_offset:
            n_row = row + row_offset
            n_col = col + col_offset

            if 0 <= n_row < m and 0 <= n_col < n:
                self._dfs(n_row, n_col, grid, m, n)


input_2 = [
    [0,0,0,0],
    [1,0,1,0],
    [0,1,1,0],
    [0,0,0,0]]
exected = 3
actual = Solution().numEnclaves(input_2)
print(f"expected: {exected} , actual:{actual}")

input_1 = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
exected = 0
actual = Solution().numEnclaves(input_1)
print(f"expected: {exected} , actual:{actual}")