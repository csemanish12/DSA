"""
Problem Description: Given an integer N, write a program to print your name N times.

Examples
Input: N = 3
Output: Jake Jake Jake 
Explanation: Name is printed 3 times.

Input: N = 1
Output: Jake 
Explanation: Name is printed once.
            
"""

class Solution:
    def print_n_times(self, n, count=0):
        if n == count:
            return
        
        print("Jake", end=" ")
        self.print_n_times(n, count+1)


input_1 = 1
Solution().print_n_times(input_1)
print("")
input_1 = 3
Solution().print_n_times(input_1)
print("")
        
"""
Time complexity: O(n)
- we print the name exactly n times

Space complexity: O(n)
- n stack space used, because we had to call function n times.
"""