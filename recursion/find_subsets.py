"""
Given an integer array nums that may contain duplicates, return all possible
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]


Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
"""
from typing import List


class Solution:
    """
    Brute Force
    1. generate all subsets using pick and not pick method.
    2. use set data structure to keep unique subsets
    Time Complexity: O( 2^n *(k log (x) )). 2^n  for generating every subset and k* log( x)  to
                     insert every combination of average length k in a set of size x.
                     After this, we have to convert the set of combinations back into a list of
                     list /vector of vectors which takes more time.

    Space Complexity:  O(2^n * k) to store every subset of average length k.
                       Since we are initially using a set to store the answer another O(2^n *k) is also used.

    Better Approach
    1. sort the array
    2. create unique array of multiple sizes. This is where we can avoid taking duplicates.
    eg: you create array of size 2 =  [1,2], now while creating another array of size 2 , we don't pick
    the element 2.

    Time Complexity: O(2^n) for generating every subset and O(k)  to insert every subset in another
                     data structure if the average length of every subset is k. Overall O(k * 2^n).

    Space Complexity: O(2^n * k) to store every subset of average length k. Auxiliary space is O(n)
                      if n is the depth of the recursion tree.
    """
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        self.subsets(0, [], nums, n, ans)

        return ans

    def subsets(self, index, subset_holder, nums, n, ans):
        ans.append(subset_holder[:])
        for i in range(index, n):
            if i != index and nums[i] == nums[i - 1]:
                continue

            subset_holder.append(nums[i])
            self.subsets(i + 1, subset_holder, nums, n, ans)
            subset_holder.pop()
