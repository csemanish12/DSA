"""
Problem Statement: Given an integer N, return all divisors of N.
A divisor of an integer N is a positive integer that divides N without leaving a remainder. 
In other words, if N is divisible by another integer without any remainder, 
then that integer is considered a divisor of N.

Examples
Input: N = 36
Output: [1, 2, 3, 4, 6, 9, 12, 18, 36]  
Explanation: The divisors of 36 are 1, 2, 3, 4, 6, 9, 12, 18, 36.

Input: N = 12
Output: [1, 2, 3, 4, 6, 12]
Explanation: The divisors of 12 are 1, 2, 3, 4, 6, 12.


sample: 20
1 * 20
2 * 10
4 * 5
sqrt is somewhere around 4.xxx
after square root, divisors are basically reversed
5 * 4
10 * 2
20 * 1

say 20 % 4 == 0
then its mirror would be a divisor too
20 / 4 = 5
20 / 5 = 4

"""
import math


class Solution:
    def print_all_divisors(self, n: int):
        result = []
        
        for i in range(1, int(math.sqrt(n)) + 1):
            quotient, rem = divmod(n, i)
            if rem == 0:
                result.append(int(i))
                
                # append mirror divisor, quotient will be mirror divisor
                if quotient != i:
                    # avoid adding same number twice. eg: 6 * 6 = 36. 
                    result.append(quotient)
        print(result)

input_1 = 36
print(f"divisors of: {input_1} are: ")
Solution().print_all_divisors(input_1)

"""
Time Complexity: O(sqrt(N))
- we iterate from 1 till sqrt of N

Space Complexity: O(sqrt(N))
In the worst case, all numbers from 1 till sqrt of N would be divisors
so result will hold all those numbers
Every other variable will be same no matter the input, so those are constant space
and ignored
"""