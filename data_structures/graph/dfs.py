"""
Given a connected undirected graph represented by an adjacency list adj, which is a vector of vectors where each adj[i] represents the list of vertices connected to vertex i. Perform a Depth First Traversal (DFS) starting from vertex 0, visiting vertices from left to right as per the adjacency list, and return a list containing the DFS traversal of the graph.

Note: Do traverse in the same order as they are in the adjacency list.

Examples:

Input: adj = [[2,3,1], [0], [0,4], [0], [2]]

Output: [0, 2, 4, 3, 1]
Explanation: Starting from 0, the DFS traversal proceeds as follows: 
Visit 0 → Output: 0 
Visit 2 (the first neighbor of 0) → Output: 0, 2 
Visit 4 (the first neighbor of 2) → Output: 0, 2, 4 
Backtrack to 2, then backtrack to 0, and visit 3 → Output: 0, 2, 4, 3 
Finally, backtrack to 0 and visit 1 → Final Output: 0, 2, 4, 3, 1
"""

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, adj):
        # code here
        visited = [False] * (len(adj) + 1)
        dfs_list = []
        start_node = 0
        self.dfs(start_node, adj, dfs_list, visited)
        return dfs_list
    
    def dfs(self, node, adj, dfs_list, visited):
        visited[node] = True
        dfs_list.append(node)
        
        for neighbor in adj[node]:
            if not visited[neighbor]:
                self.dfs(neighbor, adj, dfs_list, visited)
    

sample = [[2,3,1], [0], [0,4], [0], [2]]
print("solution:", Solution().dfsOfGraph(sample))