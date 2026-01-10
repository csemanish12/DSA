class Solution:
    def floodFill(self, grid: list[list[int]], sr: int, sc: int, color: int) -> None:
        original_color = grid[sr][sc]
        m = len(grid)
        n = len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        self._dfs(sr, sc, original_color, color, grid, m, n, visited)
    
    def _dfs(self, sr: int, sc: int, original_clor, color, grid, m, n, visited):
        grid[sr][sc] = color
        visited[sr][sc] = True

        neighbors_offset = [(1,0), (-1,0), (0,1), (0,-1)]
        for row_offset, col_offset in neighbors_offset:
            row = row_offset + sr
            col = col_offset + sc

            if (0 <= row < m and 0 <= col < n) and not visited[row][col] and grid[row][col] == original_clor:
                self._dfs(row, col, original_clor, color, grid, m, n, visited)
    




input_1 = [[0,0,0],[0,0,0]]
sr = 0
sc = 0
color = 0
expected = [[0,0,0],[0,0,0]]
Solution().floodFill(input_1, sr, sc, color)
print(f"expected:{expected}, actual:{input_1}")


input_2= [[1,1,1],[1,1,0],[1,0,1]] 
sr = 1 
sc = 1
color = 2
expected = [[2,2,2],[2,2,0],[2,0,1]]
Solution().floodFill(input_2, sr, sc, color)
print(f"expected:{expected}, actual:{input_2}")