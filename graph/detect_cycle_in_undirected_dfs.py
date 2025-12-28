class Solution:
    def isCycle(self, V: int, edges: list[list[int]]):
        visited = [False] * (V + 1)
        adj = [[] for _ in range(V+1)]

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        print("adj", adj)
        for node in range(1, V+1):
            if not visited[node]:
                if self._dfs(-1, node, adj, visited):
                    return True
        
        return False

    
    def _dfs(self, parent, node, adj, visited):
        visited[node] = True

        for neighbor in adj[node]:
            if not visited[neighbor]:
                if self._dfs(node, neighbor, adj, visited):
                    return True
            
            elif visited[neighbor] and parent != neighbor:
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


"""
Space complexity: O(V+E)
- store adjacent neighbors => node plus edges
- store visited = O(V)  => number of nodes
- stored history = O(V) => number of nodes
- stack space = O(V)

Time complexity: O(V+E)
- creating adjacent: O(E) => iterating number of edges
- traversing nodes: O(V) => in the worst case, max depth is equal to number of nodes 
"""