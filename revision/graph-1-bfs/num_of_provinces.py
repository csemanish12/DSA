from collections import deque


class Solution:
    def findCircleNum(self, grid: list[list[int]])-> int:
        m = len(grid)
        n = len(grid[0])

        # create adj
        adj  = [[] for _ in range(m)]

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1 and row != col:
                    adj[row].append(col)
        
        visited = [False for _ in range(m)]
        count = 0

        for city in range(m):
            if not visited[city]:
                self._bfs(city, visited, adj)
                count += 1
        
        return count


    def _bfs(self, city, visited, adj):
        queue = deque()
        queue.append(city)
        visited[city] = True

        while queue:
            city = queue.popleft()
            for neighbor in adj[city]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
        




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

# 0[3]
# 1[2,3]
# 2[1,3]
# 3[0,2]