"""
NEXT Permutation
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.



Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]


Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100
"""


class Solution:
    """
    1. find the longest prefix match.
        - we can identify next permutation by comparing the prefixes.
        - so the immediate permutation will have max number of prefix match.
        -  we can find it by finding the breaking point where number starts to increase
        - we don't want to start from first as next permutation is slightly greater. so start from 2nd last
    2. Find next greater element
        - for next permutation, it will be slightly greater and not the greatest
        - the numbers after breaking point will always be in order of large to small
        - can find it by searching from last
    3. Rearrange remaining element in sorting order
        - once next greater element is replaced with break point element, the remaining element is already
          in order (larger to smaller)
        - we only need to reverse the these elements to get next permutation
    """
    def get_next_permutation(self, nums: list):
        index = -1
        n = len(nums)

        # find break point
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                index = i
                break
        print("index is:", index)
        print("index number:", nums[index])

        if index == -1:
            nums.reverse()
            # no break point indicates, this the last member of the permutations and so return the first member
            return

        # find immediate greater element
        for i in range(n-1, index, -1):
            if nums[i] > nums[index]:
                print("greater next:", nums[i])
                nums[i], nums[index] = nums[index], nums[i]
                print("nums after replace:", nums)
                break

        # rearrange the remaining element in ascending order
        nums[index+1:n + 1] = reversed(nums[index+1:n + 1])


given_input_1 = [1, 2, 3]
given_input_2 = [2, 1, 5, 4, 3, 0, 0]
given_input_3 = [3, 2, 1]
given_input_4 = [1, 3, 2]

s = Solution()
s.get_next_permutation(given_input_1)
print("output:", given_input_1)

s.get_next_permutation(given_input_2)
print("output:", given_input_2)

s.get_next_permutation(given_input_3)
print("output:", given_input_3)

print("given input:", given_input_4)
s.get_next_permutation(given_input_4)
print("output:", given_input_4)

