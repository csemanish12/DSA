from collections import deque

class Solution:
    def bfs(self, adj: list[list[int]])-> list[int]:
        visited = [False for _ in range(len(adj))]
        traversed = []
        queue = deque()

        queue.append(0)
        visited[0] = True

        while queue:
            node = queue.popleft()
            traversed.append(node)
            neighbors = adj[node]

            for neighbor in neighbors:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True

        return traversed
    
input_1 = [[2, 3, 1], [0], [0, 4], [0], [2]]
expected = [0, 2, 3, 1, 4]
output = Solution().bfs(input_1)
print(f"expected:{expected}, actual: {output}")

input_2 = [[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]
expected = [0, 1, 2, 3, 4]
output = Solution().bfs(input_2)
print(f"expected:{expected}, actual: {output}")