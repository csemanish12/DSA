class Solution:
    def floodFill(self, grid: list[list[int]], sr: int, sc: int, color: int)-> list[list[int]]:
        m = len(grid)
        n = len(grid[0])
        original_color = grid[sr][sc]
        visited = [[False for _ in range(n)] for _ in range(m)]

        self._dfs(sr, sc, grid, visited, color, original_color)
    
    def _dfs(self, sr: int, sc: int, grid: list[list[int]], visited: list[list[bool]], color: int, original_color: int)-> None:
        # change to new color
        grid[sr][sc] = color
        visited[sr][sc] = True

        # find neighbors
        neighbors = [(1,0), (-1,0), (0,1), (0,-1)]
        m = len(grid)
        n = len(grid[0])

        for n_row, n_col in neighbors:
            row = sr + n_row
            col = sc + n_col

            if (0 <= row < m and 0 <= col < n) and not visited[row][col] and grid[row][col] == original_color:
                self._dfs(row, col, grid, visited, color, original_color)
    





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