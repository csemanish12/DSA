class Solution:
    def isCycle(self, vertices: int, edges: list[list[int]]) -> bool:
        visited = [False for _ in range(vertices+1)]

        # create adjacent nodes
        adj = [[] for _ in range(vertices+1)]

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # do dfs on each vertex
        for vertex in range(vertices+1):
            if not visited[vertex]:
                if self._dfs(vertex, -1, visited, adj):
                    return True

        return False 

    def _dfs(self, vertex: int, parent: int, visited: list[bool], adj: list[list]) -> bool:
        visited[vertex] = True

        for neighbor in adj[vertex]:
            if not visited[neighbor]:
                self._dfs(neighbor, vertex, visited, adj)
            
            elif neighbor != parent:
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