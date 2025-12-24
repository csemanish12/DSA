"""
Given an undirected graph with V vertices and E edges, represented as a 2D vector edges[][], where each entry edges[i] = [u, v] denotes an edge between vertices u and v, determine whether the graph contains a cycle or not.

Note: The graph can have multiple component.

Examples:

Input: V = 4, E = 4, edges[][] = [[0, 1], [0, 2], [1, 2], [2, 3]]
Output: true
Explanation: 
 
1 -> 2 -> 0 -> 1 is a cycle.
Input: V = 4, E = 3, edges[][] = [[0, 1], [1, 2], [2, 3]]
Output: false
Explanation: 
 
No cycle in the graph.
Constraints:
1 ≤ V, E ≤ 105
0 ≤ edges[i][0], edges[i][1] < V
"""

from collections import deque

class Solution:

    def isCycle(self, V, edges):
		#Code here
		# create adjcency list
        adj = [[] for _ in range(V+1)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
		
        visited = [False for _ in range(V+1)]
        queue = deque()

        for node in range(1, V+1):
            if not visited[node]:
                if self._bfs(node, adj, queue, visited):
                    return True
        
        return False
            
    def _bfs(self, node, adj, queue, visited):
        queue.append((node, -1))
        visited[node] = True
		
        while queue:
            node, parent = queue.popleft()
            neighbors = adj[node]
            for neighbor in neighbors:
                if not visited[neighbor]:
                    queue.append((neighbor, node))
                    visited[neighbor] = True
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
Time complexity: O(2E). (E=Number of edge)
- creating adjacency list: O(E)
- bfs traversal: O(2E)
  - its undirected edge, so its both ways. hence twice of edges
Space complexity: O(V) (V= Numer of vertices)
- visited array of size V
"""