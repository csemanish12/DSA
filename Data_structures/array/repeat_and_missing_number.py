"""
You are given a read only array of n integers from 1 to n.

Each integer appears exactly once except A which appears twice and B which is missing.

Return A and B.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Note that in your output A should precede B.

Example:

Input:[3 1 2 5 3]

Output:[3, 4]
"""


class Solution:
    def get_repeated_and_missing_number(self, nums):
        n = len(nums)
        natural_number_sum = (n * (n+1))/2
        natural_number_square_sum = (n * (n+1) * (2*n+1)) / 6
        sum = 0
        square_sum = 0
        for i in nums:
            sum += i
            square_sum += i * i

        val1 = sum - natural_number_sum
        val2 = square_sum - natural_number_square_sum
        val2 = val2/val1

        repeated = int((val1 + val2)/2)
        missing = int(repeated - val1)

        return repeated, missing


s = Solution()

input_1 = [3, 1, 2, 5, 3]
print("output 1:", s.get_repeated_and_missing_number(input_1))

