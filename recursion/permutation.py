"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]


Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""
from typing import List


class Solution:
    """
    Using swapping method
    Time complexity: n! * n
    space complexity: n
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        self.permute_helper(0, nums, n, ans)

        return ans

    def permute_helper(self, index, arr, n, ans):
        if index == n:
            ans.append(arr[:])
            return

        for i in range(index, n):
            arr[i], arr[index] = arr[index], arr[i]
            self.permute_helper(index + 1, arr, n, ans)
            arr[i], arr[index] = arr[index], arr[i]


