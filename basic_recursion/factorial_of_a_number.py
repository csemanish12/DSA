"""
Problem Statement: Given a number X,  print its factorial.

To obtain the factorial of a number, it has to be multiplied by all the whole numbers preceding it. More precisely X! = X*(X-1)*(X-2) … 1.

Note: X  is always a positive number. 

Examples
Example 1:
Input: X = 5
Output: 120
Explanation: 5! = 5*4*3*2*1

Example 2:
Input: X = 3
Output: 6
Explanation: 3!=3*2*1
"""

class Solution:
    def factorial(self, n: int)-> int:
        if n == 1:
            return 1
        return n * self.factorial(n-1)


input_1 = 5
print(f"factorial of {input_1} is {Solution().factorial(input_1)}")


"""
Time complexity: O(n)
- we recursively call n times (from n till 1)

Space complexity: O(n)
- we recursively call n times and hence utilize n stack space
"""