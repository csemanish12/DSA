class Solution:
    def maxPoints(self, mat: list[list[int]]) -> int:
        n = len(mat)
        dp = [[-1 for _ in range(len(mat[0]))] for _ in range(n)]
        return self._max_point(n-1, -1, mat, dp)
    
    def _max_point(self, day: int, last_activity: int, mat: list[list[int]], dp: list[list[int]]) -> int:
        if dp[day][last_activity] != -1:
            return dp[day][last_activity]
        
        if day < 0:
            return 0
        
        max_point = 0
        for activity in range(len(mat[day])):
            if activity == last_activity:
                continue
            point = mat[day][activity] + self._max_point(day-1, activity, mat, dp)
            max_point = max(max_point, point)
        
        dp[day][last_activity] = max_point
        return max_point

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
Time complexity: O(N * M * 4) = O(N * M)
- where N is number of days
- M are number of activities
- 4  is the value of activitie picked/not picked

Space complexity: O(N * M) + O(N) = O(N * M)
- O(N * 4) is for dp array
- O(N) is for recursion stack space
"""