"""
Problem Statement: Given a number ‘N’, find out the sum of the first N natural numbers .

Examples
Input: N=5
Output: 15
Explanation: 1+2+3+4+5=15

Input: N=6
Output: 21
Explanation: 1+2+3+4+5+6=15
"""
class Solution:
    def find_sum(self, n):
        if n == 1:
            return 1
        return n + self.find_sum(n-1)


input_1 = 5
print(f"sum of first {input_1} numbers is {Solution().find_sum(input_1)}")

input_1 = 6
print(f"sum of first {input_1} numbers is {Solution().find_sum(input_1)}")

"""
Time complexity: O(N)
- we recursively call from N till 1. 

Space complexity: O(N)
- we have N recursive calls and hence use N stack space 

"""