"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.



Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]


Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.


Follow up: Could you come up with a one-pass algorithm using only constant extra space?
"""

from typing import List


class Solution:
    """
    Using Dutch national flag algo.
    0 --- low -1 = all zeroes
    low --- mid-1 = all ones
    mid --- high = random (unsorted)  -- the area that we will be sorting
    high+1 --n-1 = all 2s
    """

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        mid = 0
        high = len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[mid], nums[low] = nums[low], nums[mid]
                mid += 1
                low += 1

            elif nums[mid] == 1:
                mid += 1

            elif nums[mid] == 2:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1


s = Solution()

input_1 = [2, 0, 2, 1, 1, 0]
print("before sort:", input_1)
s.sortColors(input_1)
print("after sort:", input_1)

input_2 = [2, 0, 1]
print("before sort:", input_2)
s.sortColors(input_2)
print("after sort:", input_2)
