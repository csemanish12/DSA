class Solution:
    def __init__(self):
        self.m = None
        self.n = None

        self.neighbors = [(1,0), (-1,0), (0,1), (0,-1)]

    def numEnclaves(self, grid: list[list[int]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])

        # mark border 1s to temp 
        # left column and right column
        for row in range(self.m):
            self._dfs(row, 0, grid)
            self._dfs(row, self.n - 1, grid)

        # top row and bottom row
        for col in range(self.n):
            self._dfs(0, col, grid)
            self._dfs(self.m-1, col, grid)
        
        count = 0
        # count the remaining ones
        for row in range(self.m):
            for col in range(self.n):
                if grid[row][col] == 1:
                    count += 1
        
        return count
    
    def _dfs(self, row: int, col: int, grid: list[list[int]]):
        if grid[row][col] == 0:
            return
        
        grid[row][col] = -1

        for offset_row, offset_col in self.neighbors:
            n_row = row + offset_row
            n_col = col + offset_col

            if (0 <= n_row < self.m - 1 and 0 <= n_col < self.n -1) and grid[n_row][n_col] == 1:
                self._dfs(n_row, n_col, grid)




input_2 = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
exected = 3
actual = Solution().numEnclaves(input_2)
print(f"expected: {exected} , actual:{actual}")

input_1 = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
exected = 0
actual = Solution().numEnclaves(input_1)
print(f"expected: {exected} , actual:{actual}")