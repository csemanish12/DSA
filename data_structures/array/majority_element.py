"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.



Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2


Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109


Follow-up: Could you solve the problem in linear time and in O(1) space?
"""
from typing import List


class Solution:
    """
    1. apply moore's voting algo
        - iterate from 0 - n
        take first element and set its count to 1
        - if different element found, decrease its count
        - if same element found, increase its count
        - if count == 0, means that element cannot be majority in the give subset, as its occurrence was
          negated by other elements
    2. if array does not have majority element, then an extra loop to ensure that element found at the end
    of first loop is actually majority element
    """
    def majorityElement(self, nums: List[int]) -> int:
        elem = nums[0]
        count = 1
        for i in range(1, len(nums)):

            if nums[i] == elem:
                count += 1
            else:
                count -= 1

            if count == 0:
                elem = nums[i]
                count = 1

        return elem


s = Solution()

input_1 = [2, 8, 8, 1, 1, 2, 2, 8]
print("output 1:", s.majorityElement(input_1))

input_2 = [3, 2, 3]
print("output:", s.majorityElement(input_2))

input_3 = [6, 5, 5]
print("output 3:", s.majorityElement(input_3))