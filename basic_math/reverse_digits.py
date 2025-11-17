"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1
"""

class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return x
        
        sign = 1 if x > 0 else -1

        x = abs(x)
        reversed = 0

        while x > 0:
            x, remainder = divmod(x, 10)
            reversed = reversed * 10 + remainder
                
        if reversed > 2 ** 31:
            return 0

        reversed = reversed * sign       

        return reversed


solution = Solution()

input_1 = 120
print(f"reverse of {input_1} is ", solution.reverse(input_1))

input_2 = -231
print(f"reverse of {input_2} is ", solution.reverse(input_2))

input_2 = 1534236469
print(f"reverse of {input_2} is ", solution.reverse(input_2))


"""
Time complexity: O(Log10N)
- it depends on number of digits in the given number. in the worse case, N is multiple of 10.
- to go over all the digits by dividing it by 10, will take log10N operations
- an additional iteration to make it 0, to satisfy loop condition
- so time complexity is O(log10N + 1) == O(Log10N)

Space complexity: O(1)
- no matter the number of digits in the input, the result is stored in single variable. 

"""