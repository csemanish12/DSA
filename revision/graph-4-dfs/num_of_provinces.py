class Solution:
    def findCircleNum(self, connected_grid: list[list[int]]) -> int:
        # create adjacency matrix
        m = len(connected_grid)
        n = len(connected_grid[0])
        adj = [[] for _ in range(m)]


        for row in range(m):
            for col in range(n):
                if row != col and connected_grid[row][col] == 1:
                    adj[row].append(col)
        
        visited = [False for _ in range(m)]
        num_of_provinces = 0
        for city in range(m):
            if not visited[city]:
                self._dfs(city, adj, visited)
                num_of_provinces += 1

        return num_of_provinces

    def _dfs(self, city: int, adj: list[list[int]], visited: list[bool]) -> None:
        visited[city] = True
        
        for neighbor in adj[city]:
            if not visited[neighbor]:
                self._dfs(neighbor, adj, visited)



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