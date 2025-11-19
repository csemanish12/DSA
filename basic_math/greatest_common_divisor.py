"""
You are given an integer n. Your task is to compute the GCD (greatest common divisor) of two values:

sumOdd: the sum of the first n odd numbers.

sumEven: the sum of the first n even numbers.

Return the GCD of sumOdd and sumEven.

 

Example 1:

Input: n = 4

Output: 4

Explanation:

Sum of the first 4 odd numbers sumOdd = 1 + 3 + 5 + 7 = 16
Sum of the first 4 even numbers sumEven = 2 + 4 + 6 + 8 = 20
Hence, GCD(sumOdd, sumEven) = GCD(16, 20) = 4.

Example 2:

Input: n = 5

Output: 5

Explanation:

Sum of the first 5 odd numbers sumOdd = 1 + 3 + 5 + 7 + 9 = 25
Sum of the first 5 even numbers sumEven = 2 + 4 + 6 + 8 + 10 = 30
Hence, GCD(sumOdd, sumEven) = GCD(25, 30) = 5.


"""

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        return n
    
    def gcdOfUnrelatedNumber(self, n1: int, n2: int) -> int:
        if n1 > n2:
            small_number, big_number = n1, n2
        else:
            small_number, big_number = n2, n1
        # eucleadean algorithm
        while small_number > 0:
            mod_result = big_number % small_number
            small_number, big_number = mod_result, small_number
        
        return big_number


s= Solution()
input_1 = 4
print(f"gcd of odd and even sum for {input_1} is: ", s.gcdOfOddEvenSums(input_1))

input_2 = (45, 60)
print(f"gcd of {input_2} is: ", s.gcdOfUnrelatedNumber(input_2[0], input_2[1]))

"""
Explanation:
1. sum of n odd numbers starting from 1 is = n2 (from arithmetic progression)
2. sum of n even numbers starting from 1 is = n (n + 1)
3. Eucledean algo to find gcd:
   eg to find gcd of 47, 37, we use a, b mod a where a is smaller than b
   gcd (37, 47 % mod 37) = gcd (37, 10)
   gcd (10, 37 mod 10) = gcd(10, 7)
   gcd(7, 10 mod 7) = gcd(7, 3)
   gcd(3, 7 mod 3) = gcd (3, 1)
   gcd(1, 3 mod 1) = gcd(1,0)
   so the gcd of 37 and 47 is 1

   This is for positive integers only.
   Time complexity: O(log(min(a,b)))
   - Each step reduces the problem size by at least half (on average). 
   - After one modulo operation, the remainder is always less than half of the divisor in most cases,
   - leading to logarithmic behavior.
   Space complexity: 

in this case, when we talk about even and odd numbers,
even = n2 + n (lets look closely)
- value of even sum is square of n , plus n
- this means, it is divisble by n. 
odd = n2
- vlaue of odd is simply squre of n
- this means, it is also divisible by n

hence, gcd of oddsum and evensum is n

"""