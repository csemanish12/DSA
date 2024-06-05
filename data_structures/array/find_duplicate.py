"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.



Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
Example 3:

Input: nums = [3,3,3,3,3]
Output: 3


Constraints:

1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.


Follow up:

How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem in linear runtime complexity?
"""
from typing import List


class Solution:
    """
    Intuition:
    - The values are between 1 and N, so they can be thought of as indexes.
    - when we iterate over them as indexes, we will reach a cycle as two index will point to same number
    - This is a linked list(cycle) problem
    - Solved using Floyd's algo of slow and fast point
    - slow moves 1 step, fast moves 2 step. When they intersect for the first time,
    - take another slow and start iterating from start and when it meets with prev slow, that is the duplicate number
    """
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow


s = Solution()

input_1 = [3, 1, 3, 4, 2]
print("output:", s.findDuplicate(input_1))

input_2 = [4, 1, 3, 2, 2]
print("output:", s.findDuplicate(input_2))

input_3 = [3, 3, 3, 3, 3]
print("output:", s.findDuplicate(input_3))
