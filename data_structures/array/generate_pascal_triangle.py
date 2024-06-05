"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

1
1 1
1 2 1
1 3 3 1
1 4 6 4 1

Example 1:

Input: numRows = 5 (num of rows, num of sublists)
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]

"""
from typing import List


class Solution:
    """
    Approach 1:
    If num of rows is 1, return [[1]]
    Otherwise, iterate over the range of num of rows.
    the first element of new list will be first element of previous list
    iterate over all the elements of prev list and add the current element and previous element.
    Begin the iteration from index 1 and end it at len of prev list
    Once the iteration is completed, append the last element of prev list in the new list.
    """
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        if numRows == 1:
            return result

        for row in range(1, numRows):
            prev_row_elements = result[row-1]
            new_row_elements = [prev_row_elements[0]]
            for i in range(1, len(prev_row_elements)):
                new_row_elements.append(prev_row_elements[i] + prev_row_elements[i-1])
            new_row_elements.append(prev_row_elements[-1])
            result.append(new_row_elements)

        return result


example_1 = 1
example_2 = 2
example_3 = 5

solution = Solution()

result_1 = solution.generate(example_1)
print("result 1:", result_1)

result_2 = solution.generate(example_2)
print("result 2:", result_2)

result_3 = solution.generate(example_3)
print("result 1:", result_3)