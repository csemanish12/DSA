"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
frequency
 of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.



Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []


Constraints:

1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40
"""
import copy
from typing import List


class Solution:
    """
    Pick and not pick approach
    Time Complexity: O(2^t * k) where t is the target, k is the average length
    Reason: Assume if you were not allowed to pick a single element multiple times,
            every element will have a couple of options: pick or not pick which is 2^n different
            recursion calls, also assuming that the average length of every combination generated is k.
            (to put length k data structure into another data structure)

    Why not (2^n) but (2^t) (where n is the size of an array)?
    Assume that there is 1 and the target you want to reach is 10 so 10 times you can “pick or not pick” an element.

    Space Complexity: O(k*x), k is the average length and x is the no. of combinations
    """
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        ans = []
        self.__exhaustively_search(candidates, n, 0, [], target, ans)
        return ans

    def __exhaustively_search(self, candidates, n, index, picked, target, ans):
        if index == n:
            if target == 0:
                ans.append(copy.deepcopy(picked))
            return

        if candidates[index] <= target:
            picked.append(candidates[index])
            self.__exhaustively_search(candidates, n, index, picked, target - candidates[index], ans)
            picked.pop()

        self.__exhaustively_search(candidates, n, index+1, picked, target, ans)


s = Solution()
input_1 = [2, 3, 6, 7]
target_1 = 7
print("output 1:", s.combinationSum(input_1, target_1))


s = Solution()
input_2 = [2, 3, 5]
target_2 = 8
print("output 2:", s.combinationSum(input_2, target_2))
