"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).



Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25


Constraints:

-100.0 < x < 100.0
-231 <= n <= 231-1
n is an integer.
Either x is not zero or n > 0.
-104 <= xn <= 104
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        if n < 0:
            nn = -1 * n
        else:
            nn = n

        while nn > 0:
            if nn % 2 == 1:
                ans = ans * x
                nn = nn - 1
            else:
                x = x * x
                nn = nn / 2

        if n < 0:
            ans = 1 / ans

        return float(ans)


s = Solution()
input_1_x = 2
input_1_n = 10
print("output 1:", s.myPow(input_1_x, input_1_n))

input_2_x = 2
input_2_n = -2
print("output 2:", s.myPow(input_2_x, input_2_n))