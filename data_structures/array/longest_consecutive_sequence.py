"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.



Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9


Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
from typing import List


class Solution:
    """
    start from lowest. There can be multiple lowest.
    - if num -1 does not exist in set, it means it may be the lowest
    - 100,101,103, 4,5,6
    - there are two lowest here, 100 and 4. Longest subsequence will either start from 100 or 4
    - num - 1 does not exist for both 100 and 4
    increase and check if it exists in set, increase the count if it does

    """
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        st = set(nums)
        longest = 1

        for it in st:
            if it - 1 not in st:
                x = it
                count = 1
                while x + 1 in st:
                    count += 1
                    x += 1
                longest = max(longest, count)

        return longest


s = Solution()

input_1 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
print("output 1:", s.longestConsecutive(input_1))
