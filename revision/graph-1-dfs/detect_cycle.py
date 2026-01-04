class Solution:
    def isCycle(self, V: int, edges: list[list[int]]) -> bool:
        
        adj = [[] for _ in range(V+1)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = [False for _ in range(V+1)]

        for node in range(1, V+1):
            if not visited[node]:
                if self._dfs(node, -1, adj, visited):
                    return True
        
        return False

    def _dfs(self, node: int, parent: int, adj: list[list[int]], visited: list[bool]) -> bool:
        visited[node] = True

        neighbors = adj[node]

        for neighbor in neighbors:
            if not visited[neighbor]:
                self._dfs(neighbor, node, adj, visited)
            
            elif visited[neighbor] and neighbor != parent:
                # cycle is detected
                return True
        
        return False




vertices = 8
e = [[1, 2], [2 ,3],[4, 5],[5, 6],[4, 6],[7, 8]]
expected = True
actual = Solution().isCycle(vertices, e)
print(f"expected: {expected}, actual:{actual}")


vertices = 5
e = [[1, 2], [2 ,3],[3, 4],[4, 5]]
expected = False
actual = Solution().isCycle(vertices, e)
print(f"expected: {expected}, actual:{actual}")

vertices = 4
e = [[0, 1], [0, 2], [1, 2], [2, 3]]
expected = True
actual = Solution().isCycle(vertices, e)
print(f"expected: {expected}, actual:{actual}")