from typing import List
from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        # find all 0s and they will be starting point
        nodes = []
        for row in range(m):
            for col in range(n):
                if board[row][col] == "O":
                    nodes.append((row, col))
        
        visited_node_dict = {}

        # pick visited and check if surrounding nodes are all x
        # not at edge means, it is surrounded by X

        for node in nodes:
            if visited_node_dict.get(node) is not True:
                self._bfs(node, visited_node_dict, board, m, n)
    
    def _bfs(self, node, visited: dict, grid, m,n):
        captured_nodes = []
        can_be_captured = True
        neighbors = [(1,0), (-1,0), (0,1), (0,-1)]

        queue = deque()
        queue.append(node)
        visited[node] = True

        while queue:
            curr_row, curr_col = queue.popleft()
            if self._is_at_edge(curr_row, curr_col, m, n):
                can_be_captured = False
            captured_nodes.append((curr_row, curr_col))
            for n_row, n_col in neighbors:
                row = curr_row + n_row
                col = curr_col + n_col
                
                if not (0 <= row < m and 0 <= col < n) or grid[row][col] == "X":
                    continue
                
                if grid[row][col] == "O" and visited.get((row,col), False) is False:
                    queue.append((row, col))
                    visited[(row,col)] = True


        if can_be_captured:
            for row, col in captured_nodes:
                grid[row][col] = "X"

    def _is_at_edge(self, row, col, m, n):
        return row in (m-1, 0) or col in (n-1, 0)



input_1 = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
expected_output = [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Solution().solve(input_1)
print(f"ex:{expected_output} \n ac:{input_1}")

input_2 = [["X"]]
expected_output = [["X"]]
Solution().solve(input_1)
print(f"ex:{expected_output} \n ac:{input_2}")


"""
Time complexity: O(MxN)
- finding all Os => O(MxN)
- bfs for each O => O(MxN) => worst case, all cell have zero
hence, O(MxN) + O(MxN) => O(MxN)

Space complexity: O(MxN)
- store all zeroes => O(MxN) => worst case: everything is zero
- visited node dict => O(MxN) => worst case: everything is zero
- queue => O(min(M,N)) => BFS level width
- captured node => O(MxN) => worst case: everything is zero
hence, O(MxN) + O(MxN) + O(min(M,N)) + O(MxN) => O(MxN)

"""