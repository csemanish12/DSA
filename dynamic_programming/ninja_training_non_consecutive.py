"""
Geek is going for a training program for n days. He can perform any of these activities: Running, Fighting, and Learning Practice. Each activity has some point on each day. As Geek wants to improve all his skills, he can't do the same activity on two consecutive days. Given a 2D matrix mat[][], where mat[i][0], mat[i][1], and mat[i][2] represent the merit points for Running, Fighting, and Learning on the i-th day, determine the maximum total merit points Geek can achieve .

Example:

Input: mat[][]= [[1, 2, 5],
               [3, 1, 1], 
               [3, 3, 3]]
Output: 11
Explanation: Geek will learn a new move and earn 5 point then on second day he will do running and earn 3 point and on third day he will do fighting and earn 3 points so, maximum merit point will be 11.
Input: mat[][]= [[1, 1, 1],
               [2, 2, 2],
               [3, 3, 3]]
Output: 6
Explanation: Geek can perform any activity each day while adhering to the constraints, in order to maximize his total merit points as 6.
Input: mat[][]= [[4, 2, 6]]
Output: 6
Explanation: Geek will learn a new move to make his merit points as 6.
Constraint:
1 ≤ n ≤ 105   
1 ≤  arr[i][j] ≤ 100
"""

class Solution:
    def maxPoints(self, mat: list[list[int]]) -> int:
        dp = [[-1 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        return self._max_points(len(mat) - 1, -1, mat, dp)

    def _max_points(self, day: int, last_activity: int, mat: list[list[int]], dp: list[list[int]]):
        if dp[day][last_activity] != -1:
            return dp[day][last_activity]
        
        # base condition, when we reach day 0
        if day == 0:
            max_points = 0
            for activity_index in range(len(mat[day])):
                max_points = max(max_points, mat[day][activity_index])

            dp[day][last_activity] = max_points
            return max_points 

        max_points = 0
        for activity_index in range(len(mat[day])):
            if activity_index == last_activity:
                continue

            points = mat[day][activity_index] + self._max_points(day - 1, activity_index, mat, dp)
            max_points = max(max_points, points)
        
        dp[day][last_activity] = max_points
        return max_points


input1 = [[1, 1, 1],
               [2, 2, 2],
               [3, 3, 3]]
expected_output = 6
actual_output = Solution().maxPoints(input1)
print(f"expected:{expected_output}, actual:{actual_output}")

input1 = [[1, 2, 5],
               [3, 1, 1], 
               [3, 3, 3]]

expected_output = 11
actual_output = Solution().maxPoints(input1)
print(f"expected:{expected_output}, actual:{actual_output}")


"""
Time Complexity: O(n × 4 × 3) = O(n)

There are n days and 4 possible values for last (-1, 1, 2, 3).
For each state, we loop through 3 possible activities.

Space Complexity: O(n × 4) + O(n) for recursion stack
O(n × 4) for the DP table
O(n) for recursion call stack in the worst case

"""