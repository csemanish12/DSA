from collections import deque
from typing import List


class Solution:
    """
    Do a traversal from each node. This traversal will ensure it visits all its connected nodes.
    All the connected node forms an island and increase the island count by 1.
    The next time you find a node which is not visited yet, start traversal from that node again and
    increase the count by 1.
    """
    def __init__(self):
        self.row_size = None
        self.column_size = None

    def get_num_of_islands(self, grid: List[List[str]]) -> int:
        island_count = 0
        visited = dict()
        queue = deque()
        self.row_size = len(grid)
        self.column_size = len(grid[0])

        for row in range(self.row_size):
            for column in range(self.column_size):
                land = (row, column)
                if grid[row][column] == "1" and visited.get(land, 0) == 0:
                    # Traverse from this node. It indicates that we found land which belongs in new island
                    self.bfs(land, visited, queue, grid)
                    island_count += 1

        return island_count

    def bfs(self, land, visited, queue, grid):
        visited[land] = 1
        queue.append(land)

        while len(queue) > 0:
            next_land = queue.popleft()
            row, column = next_land

            # find neighbour (horizontal and vertical)
            neighbours = [(row - 1, column), (row + 1, column), (row, column - 1), (row, column + 1)]
            for neighbor_row, neighbor_column in neighbours:
                neighbor_land = (neighbor_row, neighbor_column)

                if (0 <= neighbor_row < self.row_size) and (0 <= neighbor_column < self.column_size) and \
                        visited.get(neighbor_land, 0) == 0 and grid[neighbor_row][neighbor_column] == "1":
                    visited[neighbor_land] = 1
                    queue.append(neighbor_land)


case_1 = [["1", "1", "1", "1", "0"],
          ["1", "1", "0", "1", "0"],
          ["1", "1", "0", "0", "0"],
          ["0", "0", "0", "0", "0"]]

case_2 = [["1", "1", "0", "0", "0"],
          ["1", "1", "0", "0", "0"],
          ["0", "0", "1", "0", "0"],
          ["0", "0", "0", "1", "1"]]

s = Solution()
print("count for case 1 is:", s.get_num_of_islands(case_1))
print("count for case 2 is:", s.get_num_of_islands(case_2))
