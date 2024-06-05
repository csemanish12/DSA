"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        n = len(nums)
        for i in range(n):
            num_dict[nums[i]] = i

        for i in range(n):
            required_number = target - nums[i]
            required_number_index = num_dict.get(required_number)
            if required_number_index is not None and required_number_index != i:
                return [i, required_number_index]


s = Solution()

input_1 = [2, 7, 11, 15]
print("solution:", s.twoSum(input_1, 9))
