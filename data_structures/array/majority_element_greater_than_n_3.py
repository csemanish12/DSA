"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.



Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]


Constraints:

1 <= nums.length <= 5 * 104
-109 <= nums[i] <= 109


Follow up: Could you solve the problem in linear time and in O(1) space?
"""
from typing import List


class Solution:
    """
    At max there can be only two elements whose count can be greater than n/3
    example:
    array size = 8
    n/3 = 2.... = 2
    greater than 2 is 3.
    3 * 3 = 9 -> exceeds array size
    3 * 2 = 6 -> within array size
    """
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1 = 0
        count2 = 0
        element1 = None
        element2 = None
        n_by_3 = len(nums) // 3
        for num in nums:
            if count1 == 0 and element2 != num:
                count1 = 1
                element1 = num
            elif count2 == 0 and element1 != num:
                count2 = 1
                element2 = num

            elif element1 == num:
                count1 += 1
            elif element2 == num:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1

        count1 = 0
        count2 = 0
        for num in nums:
            if num == element1:
                count1 += 1

            if num == element2:
                count2 += 1
        ans = []
        if count1 > n_by_3:
            ans.append(element1)

        if count2 > n_by_3:
            ans.append(element2)

        return ans


s = Solution()

input_1 = [3, 2, 3]
print("output 1:", s.majorityElement(input_1))

input_2 = [1, 2]
print("output 2:", s.majorityElement(input_2))
