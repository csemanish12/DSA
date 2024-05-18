"""
you are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.



Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.


Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109
"""
from typing import List


class Solution:
    """
    Intuition: Both arrays are sorted. So the last element of Array1 should be smaller and first element of Array2.
    Swap until you get above
    Sort both array's again
    """

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # swap till both array have
        i = m - 1
        j = 0
        while (m > 0 and i >= 0) and (n > 0 and j < n):
            if nums1[i] > nums2[j]:
                nums1[i], nums2[j] = nums2[j], nums1[i]
                i -= 1
                j += 1
            else:
                # if one element is not greater then remaining won't be. Its a sorted list
                break

        nums1[0:m] = sorted(nums1[0:m])
        nums2.sort()

        j = 0
        for index in range(m, m + n):
            nums1[index] = nums2[j]
            j += 1


s = Solution()
input_1_n1 = [1, 2, 3, 0, 0, 0]
m1 = 3
input_1_n2 = [2, 5, 6]
n1 = 3
s.merge(input_1_n1, m1, input_1_n2, n1)
print("output:", input_1_n1)

input_2_n1 = [1]
m2 = 1
input_2_n2 = []
n2 = 0
s.merge(input_2_n1, m2, input_2_n2, n2)
print("output", input_2_n1)

input_3_n1 = [0]
m3 = 0
input_3_n2 = [2]
n3 = 1
s.merge(input_3_n1, m3, input_3_n2, n3)
print("output", input_3_n1)

input_4_n1 = [1, 2, 3, 4, 5]
m4 = 5
input_4_n2 = []
n4 = 0
s.merge(input_4_n1, m4, input_4_n2, n4)
print("output", input_4_n1)

input_5_n1 = [2, 0]
m5 = 1
input_5_n2 = [1]
n5 = 1
s.merge(input_5_n1, m5, input_5_n2, n5)
print("output", input_5_n1)

input_6_n1 = [4, 0, 0, 0, 0, 0]
m6 = 1
input_6_n2 = [1, 2, 3, 5, 6]
n6 = 5
s.merge(input_6_n1, m6, input_6_n2, n6)
print("output", input_6_n1)
