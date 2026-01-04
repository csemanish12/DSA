from collections import deque

class Solution:
    def isCycle(self, V: int, edges: list[list[int]]) -> bool:
        # create adj list
        adj = [[] for _ in range(V+1)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = [False for _ in range(V+1)]

        # start bfs with all nodes
        for vertex in range(1, V+1):
            if not visited[vertex]:
                if self._bfs(vertex, visited, adj):
                    return True
            
        return False

    def _bfs(self, vertex: int, visited: list[bool], adj: list[list[int]]) -> bool:
        queue = deque()
        queue.append((vertex, -1))
        visited[vertex] = True

        while queue:
            node, parent = queue.popleft()

            for neighbor in adj[node]:
                if not visited[neighbor]:
                    queue.append((neighbor, node))
                    visited[neighbor] = True
                
                elif visited[neighbor] and neighbor != parent:
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