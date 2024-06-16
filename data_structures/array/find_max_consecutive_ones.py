"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.



Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2


Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive = 0
        current_consecutive = 0
        for num in nums:
            if num == 0:
                max_consecutive = max(current_consecutive, max_consecutive)
                current_consecutive = 0
            else:
                current_consecutive += 1
        max_consecutive = max(current_consecutive, max_consecutive)

        return max_consecutive
