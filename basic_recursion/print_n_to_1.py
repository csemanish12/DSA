"""
Problem Description: Given an integer N, write a program to print numbers from N to 1.

Examples
Input: N = 4
Output: 4, 3, 2, 1
Explanation: All the numbers from 4 to 1 are printed.

Input: N = 1
Output: 1 
Explanation: This is the base case.
"""

class Solution:
    def print_n_till_1(self, N):
        if N == 0:
            return
        
        if N == 1:
            print(N, end="")
        else:
            print(N, end=", ")

        self.print_n_till_1(N-1)

input_1 = 5
Solution().print_n_till_1(input_1)
print("")
input_2 = 1
Solution().print_n_till_1(input_2)
print("")


"""
Time complexity: O(N)
- we print N numbers

Space complexity: O(N)
- we use N stack space because we call same function N times
"""