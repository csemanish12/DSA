"""
Maximum Subarray

Given an integer array nums, find the
subarray
 with the largest sum, and return its sum.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104


Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

import math

from typing import List


class Solution:
    """
    Initialize sum to zero and move forward until you get positive value when you
    update the sum with current element. Once you get negative, re-initialize sum to zero.
    """
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -math.inf
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]

            if sum > max_sum:
                max_sum = sum

            if sum < 0:
                sum = 0

        return max_sum


s = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
s.maxSubArray(nums)
