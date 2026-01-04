class Solution:
    def findCircleNum(self, grid: list[list[int]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])

        adj = [[] for _ in range(len(grid))]

        for row in range(self.m):
            for col in range(self.n):
                if grid[row][col] == 1:
                    adj[row].append(col)
        
        visited = [False for _ in range(self.m)]
        
        number_of_provinces = 0
        for city in range(self.m):
            if not visited[city]:
                self._dfs(city, visited, adj)
                number_of_provinces += 1

        return number_of_provinces

    def _dfs(self, city: int, visited: list[bool], adj: list[list[int]]) -> None:
        visited[city] = True

        # visit the neighbors
        for neighbor in adj[city]:
            if not visited[neighbor]:
                self._dfs(neighbor, visited, adj)
    



input_1 = [[1,1,0],[1,1,0],[0,0,1]]
expected = 2
print(f"expected:{expected}, actual:{Solution().findCircleNum(input_1)}")
        

input_2 = [[1,0,0],[0,1,0],[0,0,1]]
expected = 3
print(f"expected:{expected}, actual:{Solution().findCircleNum(input_2)}")

input_3 = [
    [1,0,0,1],
    [0,1,1,0],
    [0,1,1,1],
    [1,0,1,1]]
expected = 1
print(f"expected:{expected}, actual:{Solution().findCircleNum(input_3)}")