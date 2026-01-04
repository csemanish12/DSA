"""
There are n cities. 
Some of them are connected, while some are not. 
If city a is connected directly with city b, and 
city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where 
isConnected[i][j] = 1 if the ith city and the jth city are directly connected, 
and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

 

Example 1:


Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Example 2:


Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3

"""
class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        visited = [False for _ in range(len(isConnected))]
        count = 0
        for node in range(len(isConnected)):
            if not visited[node]:
                self._dfs(node, isConnected, visited)
                count += 1
        return count
    
    def _dfs(self, node: int, isConnected: list[list[int]], visited: list) -> None:
        visited[node] = True
        neighbors = isConnected[node]
        for neighbor in range(len(neighbors)):
            if not visited[neighbor] and isConnected[node][neighbor] == 1:
                self._dfs(neighbor, isConnected, visited)


input_1 = [[1,1,0],[1,1,0],[0,0,1]]
expected = 2
print(f"expected:{expected}, actual:{Solution().findCircleNum(input_1)}")
        

input_2 = [[1,0,0],[0,1,0],[0,0,1]]
expected = 3
print(f"expected:{expected}, actual:{Solution().findCircleNum(input_2)}")

input_3 = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
expected = 1
print(f"expected:{expected}, actual:{Solution().findCircleNum(input_3)}")


"""
Time complexity: O(N^2) => number of city
- outer loop: scan all the cities
- inner loop: scans the connection with every city

Space Complexity: O(N) => number of city
- visited array stores boolean data for all cities (N)
- Recursion Stack space: O (N)
  - in the worse case, all cities form a single line
  - the max depth will be number of cities
  - hence O(N)

"""