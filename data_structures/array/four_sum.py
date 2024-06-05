"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.



Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]


Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
"""
from typing import List


class Solution:
    """
    1. Sort
    2. fix i and j
    3. move between k and l
    4. while increasing i,j,k, or decreasing l, avoid duplicates
    """
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, n):
                if j != (i+1) and nums[j] == nums[j-1]:
                    continue

                k = j+1
                l = n - 1
                while k < l:
                    sum = nums[i] + nums[j] + nums[k] + nums[l]

                    if sum == target:
                        ans.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1
                        while k < l and nums[k] == nums[k-1]:
                            k += 1
                        while k < l and nums[l] == nums[l+1]:
                            l -= 1
                    elif sum < target:
                        k += 1
                    else:
                        l -= 1

        return ans


s = Solution()

input_1 = [1, 0, -1, 0, -2, 2]
target_1 = 0
print("ans 1:", s.fourSum(input_1, target_1))