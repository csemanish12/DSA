"""
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed. All houses at this 
place are arranged in a circle. That means the first house is the neighbor 
of the last one. Meanwhile, adjacent houses have a security system connected, 
and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.
 

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [1,2,3]
Output: 3
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 1000
"""

class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        dp = {}

        return self._rob(n-1, nums, dp, n)
    
    def _rob(self, index: int, nums: list[int], dp: dict, n: int, is_last_picked=False) -> int:
        if index < 0:
            return 0
        
        if (index, is_last_picked) in dp:
            return dp[(index, is_last_picked)]

        if index == 0 and is_last_picked: 
            pick = 0
        else:
            if index == n-1:
                pick = nums[index] + self._rob(index - 2, nums, dp, n, True)
            else:
                pick = nums[index] + self._rob(index - 2, nums, dp, n, is_last_picked)
                

        not_pick = self._rob(index -1, nums, dp, n, is_last_picked)

        dp[(index, is_last_picked)] = max(pick, not_pick)

        return dp[(index, is_last_picked)]
        

input1 = [1,2,3]
expected_output = 3
actual_output = Solution().rob(input1)
print(f"expected:{expected_output}, actual:{actual_output}")


input1 = [1,2,3,1]
expected_output = 4
actual_output = Solution().rob(input1)
print(f"expected:{expected_output}, actual:{actual_output}")


"""
Time complexity: O(N)
where N is number of elements in array.
The overlapping subproblems will return the answer in constant time O(1)

Space complexity: O(N+N)
where N is number of elements in array.
N space for memo and N stack space
"""