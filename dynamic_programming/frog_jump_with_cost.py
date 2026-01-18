"""
Given an integer array height[] where height[i] represents the height of the i-th stair, 
a frog starts from the first stair and wants to reach the last stair. 
From any stair i, the frog has two options: it can either jump to the (i+1)th stair or the (i+2)th stair. 
The cost of a jump is the absolute difference in height between the two stairs. 
Determine the minimum total cost required for the frog to reach the last stair.

Example:

Input: heights[] = [20, 30, 40, 20]
Output: 20
Explanation:  Minimum cost is incurred when the frog jumps from stair 0 to 1 then 1 to 3:
jump from stair 0 to 1: cost = |30 - 20| = 10
jump from stair 1 to 3: cost = |20 - 30| = 10
Total Cost = 10 + 10 = 20
Input: heights[] = [30, 20, 50, 10, 40]
Output: 30
Explanation: Minimum cost will be incurred when frog jumps from stair 0 to 2 then 2 to 4:
jump from stair 0 to 2: cost = |50 - 30| = 20
jump from stair 2 to 4: cost = |40 - 50| = 10
Total Cost = 20 + 10 = 30
Constraints:
1 ≤ height.size() ≤ 105
0 ≤ height[i] ≤ 104

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)
"""
class Solution:
    def minCost(self, heights: list[int]) -> int:
        memo = {}
        position = 0
        cost = 0
        self._dfs(position, cost, memo, heights, len(heights))

        return memo[(position, cost)]
    
    def _dfs(self, position: int, last_cost: int, memo: dict, heights: list[int], n: int) -> int:
        if (position, last_cost) in memo:
            return memo[(position, last_cost)]
        
        if position ==  n - 1:
            return last_cost

        # get min of both paths
        cost_1, cost_2 = 999, 999
        next_position = position + 1
        if next_position < n:
            cost = last_cost + abs(heights[next_position] - heights[position])
            cost_1 = self._dfs(next_position, cost, memo, heights, n)

        next_position = position + 2
        if next_position < n:
            cost = last_cost + abs(heights[next_position] - heights[position])
            cost_2 = self._dfs(next_position, cost, memo, heights, n)
        
        memo[(position, last_cost)] = min(cost_1, cost_2)
        return memo[((position, last_cost))]
    


input1 = [20, 30, 40, 20]
expected_output = 20
actual_output = Solution().minCost(input1)
print(f"expected:{expected_output}, actual:{actual_output}")

input1 = [30, 20, 50, 10, 40]
expected_output = 30
actual_output = Solution().minCost(input1)
print(f"expected:{expected_output}, actual:{actual_output}")