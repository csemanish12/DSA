"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.



Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down


Constraints:

1 <= m, n <= 100
"""


class BruteForceSolution:
    """
    Using Recursion go over all the combinations
    """

    def uniquePaths(self, m: int, n: int) -> int:
        i = 0
        j = 0
        result = self.get_unique_path(i, j, m, n)

        return result

    def get_unique_path(self, i, j, m, n):
        if i > m or j > n:
            return 0
        if i == m - 1 and j == n - 1:
            return 1

        return self.get_unique_path(i + 1, j, m, n) + self.get_unique_path(i, j + 1, m, n)


class BetterSolution:
    """
    Using DP to store past data. Recursion will walk some paths multiple times.
    We can reduce those by saving those data
    """
    def uniquePaths(self, m: int, n: int) -> int:
        dp = []
        for i in range(m):
            row = []
            for j in range(n):
                row.append(-1)
            dp.append(row)
        i = 0
        j = 0
        result = self.get_unique_path(i, j, m, n, dp)

        return result

    def get_unique_path(self, i, j, m, n, dp):
        if i >= m or j >= n:
            return 0
        if i == m - 1 and j == n - 1:
            return 1

        if dp[i][j] != -1:
            return dp[i][j]
        dp[i][j] = self.get_unique_path(i + 1, j, m, n, dp) + self.get_unique_path(i, j + 1, m, n, dp)
        return dp[i][j]


class OptimalSolution:
    """
    Using Combination:
    m+n-2       m+n-2
      C           C
       m-1         n-1
    Explanation;
    1. There will always be m+n-2 steps to reach the goal
    2. Combination of these steps will give us the count
    """
    def uniquePaths(self, m: int, n: int) -> int:
        num_of_steps = m + n - 2
        r = m - 1
        result = 1
        for i in range(1, r+1):
            result = result * (num_of_steps - r + i) / i

        return int(result)


s = BruteForceSolution()
s_better = BetterSolution()
s_optimal = OptimalSolution()

input_1_m = 3
input_1_n = 7
print("output 1 using brute:", s.uniquePaths(input_1_m, input_1_n))
print("output 1 using better:", s_better.uniquePaths(input_1_m, input_1_n))
print("output 1 using optimal:", s_optimal.uniquePaths(input_1_m, input_1_n))

input_2_m = 3
input_2_n = 2
print("output 2 using brute:", s.uniquePaths(input_2_m, input_2_n))
print("output 2 using better:", s_better.uniquePaths(input_2_m, input_2_n))
print("output 2 using optimal:", s_optimal.uniquePaths(input_2_m, input_2_n))