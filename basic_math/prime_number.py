"""
Problem Statement: Given an integer N, check whether it is prime or not.
A prime number is a number that is only divisible by 1 and itself and the total number of divisors is 2.

Examples
                Example 1:
                Input:N = 2
               
                Output:True
                
                Explanation: 2 is a prime number because it has two divisors: 1 and 2 (the number itself).
                                        
                Example 2:
                Input:N =10                
                
                Output: False
                
                Explanation: 10 is not prime, it is a composite number because it has 4 divisors: 1, 2, 5 and 10.                            

"""
import math


class Solution:
    def is_prime(self, n):
        if n < 2:
            return False
        
        if n == 2:
            return True
        
        for num in range(2, int(math.sqrt(n)) + 1):
            if n % num == 0:
                return False
        
        return True


input_1 = 2
print(f"{input_1} is prime: {Solution().is_prime(input_1)}")

input_1 = 10
print(f"{input_1} is prime: {Solution().is_prime(input_1)}")

"""
Time complexity: O(sqrt(n))
- the loop starts from 2 to sqrt of input number.

Space complexity: O(1)
- constant space used for comparison
- won't change with input, will always remain same no matter the input
"""