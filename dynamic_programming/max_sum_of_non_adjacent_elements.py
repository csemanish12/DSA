"""
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, the only constraint 
stopping you from robbing each of them is that adjacent houses have 
security systems connected and it will automatically contact the police 
if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400
"""

class Solution:
    def rob(self, nums: list[int]) -> int:
        amount = 0
        n = len(nums)
        index = n -1
        dp = [-1 for _ in range(n)]
        robbed_amount = self._rob_next(index, nums, dp)
        return robbed_amount
    
    def _rob_next(self, index: int, nums: list[int], dp: list) -> int:
        
        if index < 0:
            return 0

        if index == 0:
            nums[0]

        if dp[index] != -1:
            return dp[index]
        

        # skip current
        pick = self._rob_next(index - 1, nums, dp)
        
        # rob current
        not_pick = nums[index] + self._rob_next(index - 2, nums, dp)

        amount = max(pick, not_pick)
        dp[index] = amount
        return dp[index]


input1 = [1,2,3,1]
expected_output = 4
actual_output = Solution().rob(input1)
print(f"expected:{expected_output}, actual:{actual_output}")

input1 = [3]
expected_output = 3
actual_output = Solution().rob(input1)
print(f"expected:{expected_output}, actual:{actual_output}")

input1 = [1,2,11,1]
expected_output = 12
actual_output = Solution().rob(input1)
print(f"expected:{expected_output}, actual:{actual_output}")


"""
Time Complexity: O(N), where N = total no. of elements in array. 
The overlapping subproblems will return the answer in constant time O(1).
Space Complexity: O(N+N), extra space used for memoization and auxiliary stack space.
"""