"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.



Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output:
[
[1,2,2],
[5]
]


Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""
import copy
from typing import List


class Solution:
    """
    Picking at all indexes

    Time Complexity:O(2^n*k)
    Reason: Assume if all the elements in the array are unique then the no. of subsequence you will get will
    be O(2^n). we also add the ds to our ans when we reach the base case that will take “k”//average space for the ds.

    Space Complexity:O(k*x)
    Reason: if we have x combinations then space will be x*k where k is the average length of the combination.
    """
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        ans = []
        self.__find_combination(candidates, n, 0, [], target, ans)

        return ans

    def __find_combination(self, candidates, n, index, picked, target, ans):
        if target == 0:
            ans.append(copy.deepcopy(picked))
            return

        for i in range(index, n):
            if candidates[i] > target:
                break

            if i != index and candidates[i] == candidates[i-1]:
                continue

            picked.append(candidates[i])
            self.__find_combination(candidates, n, i+1, picked, target - candidates[i], ans)
            picked.pop()


s = Solution()
input_1 = [10, 1, 2, 7, 6, 1, 5]
target_1 = 8
print("output: 1", s.combinationSum2(input_1, target_1))
