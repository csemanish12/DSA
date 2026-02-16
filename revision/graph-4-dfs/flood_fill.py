class Solution:
    def floodFill(self, grid: list[list[int]], sr: int, sc: int, color: int) -> None:
        n = len(grid)
        m = len(grid[0])
        starting_color = grid[sr][sc]
        visited = [[False for _ in range(m)] for _ in range(n)]
        self._fill(sr, sc, grid, starting_color, color, visited)

    def _fill(self, row: int, col: int, grid: list[list[int]], starting_color: int, color: int, visited: list[list[int]]):
        grid[row][col] = color
        visited[row][col] = True

        neighbor_offset = [(0,1), (0,-1), (1,0), (-1,0)]
        for row_offset, col_offset in neighbor_offset:
            n_row = row + row_offset
            n_col = col + col_offset

            if not (0 <= n_row < len(grid) and 0 <= n_col < len(grid[0])):
                continue
            
            if not visited[n_row][n_col] and grid[n_row][n_col] == starting_color:
                self._fill(n_row, n_col, grid, starting_color, color, visited)


# input_1 = [[0,0,0],[0,0,0]]
# sr = 0
# sc = 0
# color = 0
# expected = [[0,0,0],[0,0,0]]
# Solution().floodFill(input_1, sr, sc, color)
# print(f"expected:{expected}, actual:{input_1}")


input_2= [[1,1,1],[1,1,0],[1,0,1]] 
sr = 1 
sc = 1
color = 2
expected = [[2,2,2],[2,2,0],[2,0,1]]
Solution().floodFill(input_2, sr, sc, color)
print(f"expected:{expected}, actual:{input_2}")