"""
Given an integer array nums, return the number of reverse pairs in the array.

A reverse pair is a pair (i, j) where:

0 <= i < j < nums.length and
nums[i] > 2 * nums[j].


Example 1:

Input: nums = [1,3,2,3,1]
Output: 2
Explanation: The reverse pairs are:
(1, 4) --> nums[1] = 3, nums[4] = 1, 3 > 2 * 1
(3, 4) --> nums[3] = 3, nums[4] = 1, 3 > 2 * 1
Example 2:

Input: nums = [2,4,3,5,1]
Output: 3
Explanation: The reverse pairs are:
(1, 4) --> nums[1] = 4, nums[4] = 1, 4 > 2 * 1
(2, 4) --> nums[2] = 3, nums[4] = 1, 3 > 2 * 1
(3, 4) --> nums[3] = 5, nums[4] = 1, 5 > 2 * 1


Constraints:

1 <= nums.length <= 5 * 104
-231 <= nums[i] <= 231 - 1
"""
from typing import List


class Solution:
    """
    Adding count step before merging.
    Similar to inversion count.
    Difference: a[i] > 2*a[j], that means a[i+1] can still satisfy the condition when
    a[i] did not.
    """
    def count_reverse_pairs(self, arr, low, mid, high):
        count = 0
        right = mid + 1
        for i in range(low, mid+1):
            while right <= high and arr[i] > 2 * arr[right]:
                right += 1
            count += right - (mid + 1)
        return count

    def merge(self, arr, low, mid, high):
        """
        sorts the array in descending order
        change left_half[i] <= right_half[j] to left_half[i] >= right_half[j] for sorting in descending order
        """
        left = low  # starting index of left half
        right = mid + 1  # starting index of right half
        temp = []

        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1

        # copy the remaining elements of left, if there are any
        while left <= mid:
            temp.append(arr[left])
            left += 1

        # copy the remaining elements of right, if there are any
        while right <= high:
            temp.append(arr[right])
            right += 1

        # transferring elements from temp to array
        for i in range(low, high + 1):
            arr[i] = temp[i - low]

    def merge_sort(self, arr, low, high):
        """
        :param arr: array of numbers
        :param left_index:left index
        :param right_index:right index
        """
        count = 0
        if low >= high:
            return count

        mid = (low + high) // 2

        # sort first and second halves
        count += self.merge_sort(arr, low, mid)
        count += self.merge_sort(arr, mid + 1, high)
        count += self.count_reverse_pairs(arr, low, mid, high)
        self.merge(arr, low, mid, high)

        return count

    def reversePairs(self, nums: List[int]) -> int:
        count = self.merge_sort(nums, 0, len(nums) - 1)

        return count


s = Solution()

input_1 = [1, 3, 2, 3, 1]
print("output 1:", s.reversePairs(input_1))
