class Solution:
    def dfs(self, adj: list[list[int]])-> list[int]:
        visited = [False for _ in range(len(adj))]
        traversed = []

        self._dfs(0, adj, visited, traversed)
        return traversed
    
    def _dfs(self, node: int, adj: list[list[int]], visited: list[bool], traversed: list[int])-> None:
        visited[node] = True
        traversed.append(node)

        neighbors = adj[node]

        for neighbor in neighbors:
            if not visited[neighbor]:
                self._dfs(neighbor, adj, visited, traversed)


    
input_1 =  [[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]
expected = [0, 1, 2, 3, 4]
output = Solution().dfs(input_1)
print(f"expected:{expected}, actula: {output}")