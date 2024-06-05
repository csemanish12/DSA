"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.



Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.


Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""
from typing import List


class Solution:
    """
    Sort
    Single Iteration, compare with last element in the ans array and update or add accordingly
    """

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        for i in range(len(intervals)):
            if len(ans) == 0:
                ans.append(intervals[i])

            else:
                if ans[-1][1] >= intervals[i][0]:
                    ans[-1][1] = max(ans[-1][1], intervals[i][1])
                else:
                    ans.append(intervals[i])

        return ans


s = Solution()
input_1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
expected_Output_1 = [[1, 6], [8, 10], [15, 18]]
output_1 = s.merge(input_1)
print("input: ", input_1)
print("output: ", output_1)
print("expected: ", expected_Output_1)

input_2 = [[1, 4], [4, 5]]
expected_Output_2 = [[1, 5]]
output_2 = s.merge(input_2)
print("input: ", input_2)
print("output: ", output_2)
print("expected: ", expected_Output_2)

input_3 = [[1, 4], [1, 4]]
expected_Output_3 = [[1, 4]]
output_3 = s.merge(input_3)
print("input: ", input_3)
print("output: ", output_3)
print("expected: ", expected_Output_3)
