"""
Rat in a Maze

Consider a rat placed at (0, 0) in a square matrix of order N * N.
It has to reach the destination at (N - 1, N - 1).
Find all possible paths that the rat can take to reach from source to destination.
The directions in which the rat can move are 'U'(up), 'D'(down), 'L' (left), 'R' (right).
Value 0 at a cell in the matrix represents that it is blocked and the rat cannot move to it
while value 1 at a cell in the matrix represents that rat can travel through it.

Note: In a path, no cell can be visited more than one time.

Print the answer in lexicographical(sorted) order

Examples:

Example 1:

Input:
N = 4
m[][] = {{1, 0, 0, 0},
        {1, 1, 0, 1},
        {1, 1, 0, 0},
        {0, 1, 1, 1}}

Output: DDRDRR DRDDRR

Explanation:



The rat can reach the destination at (3, 3) from (0, 0) by two paths - DRDDRR and DDRDRR, when printed in sorted order we get DDRDRR DRDDRR.

Example 2:

Input: N = 2
       m[][] = {{1, 0},
                {1, 0}}

Output:
 No path exists and the destination cell is blocked.
"""
from typing import List


class Solution:
    """
    Approach:

    - Start at the source(0,0) with an empty string and try every possible path
      i.e upwards(U), downwards(D), leftwards(L) and rightwards(R).
    - As the answer should be in lexicographical order so it's better to try the directions in lexicographical
      order i.e (D,L,R,U)
    - Declare a 2D-array named visited because the question states that a single cell should be included only
      once in the path,so it's important to keep track of the visited cells in a particular path.
    - If a cell is in path, mark it in the visited array.
    - Also keep a check of the “out of bound” conditions while going in a particular direction in the matrix.
    - Whenever you reach the destination(n,n) it's very important to get back as shown in the recursion tree.
    - While getting back, keep on unmarking the visited array for the respective direction.Also check whether
      there is a different path possible while getting back and if yes, then mark that cell in the visited array
    """

    def findPathHelper(self, i: int, j: int, a: List[List[int]], n: int, ans: List[str], move: str,
                       vis: List[List[int]]):
        if i == n - 1 and j == n - 1:
            ans.append(move)
            return

        # downward
        if i + 1 < n and not vis[i + 1][j] and a[i + 1][j] == 1:
            vis[i][j] = 1
            self.findPathHelper(i + 1, j, a, n, ans, move + 'D', vis)
            vis[i][j] = 0

        # left
        if j - 1 >= 0 and not vis[i][j - 1] and a[i][j - 1] == 1:
            vis[i][j] = 1
            self.findPathHelper(i, j - 1, a, n, ans, move + 'L', vis)
            vis[i][j] = 0

        # right
        if j + 1 < n and not vis[i][j + 1] and a[i][j + 1] == 1:
            vis[i][j] = 1
            self.findPathHelper(i, j + 1, a, n, ans, move + 'R', vis)
            vis[i][j] = 0

        # upward
        if i - 1 >= 0 and not vis[i - 1][j] and a[i - 1][j] == 1:
            vis[i][j] = 1
            self.findPathHelper(i - 1, j, a, n, ans, move + 'U', vis)
            vis[i][j] = 0

    def findPath(self, m: List[List[int]], n: int) -> List[str]:
        ans = []
        vis = [[0 for _ in range(n)] for _ in range(n)]

        if m[0][0] == 1:
            self.findPathHelper(0, 0, m, n, ans, "", vis)
        return ans


if __name__ == '__main__':
    n = 4

    m = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]

    obj = Solution()
    result = obj.findPath(m, n)
    if len(result) == 0:
        print(-1)
    else:
        for i in range(len(result)):
            print(result[i], end=" ")
    print()
