class Solution:
    def findCircleNum(self, matrix: list[list[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        adj = [[] for _ in range(m)]

        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 1:
                    adj[row].append(col)
        
        visited = [False for _ in range(m)]
        count = 0

        for vertex in range(m):
            if not visited[vertex]:
                self._dfs(vertex, visited, adj)
                count += 1

        return count


    def _dfs(self, vertex: int, visited: list[bool], adj: list[list]) -> None:
        visited[vertex] = True

        for neighbor in adj[vertex]:
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