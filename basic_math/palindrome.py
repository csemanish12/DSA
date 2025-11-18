"""
Given an integer x, return true if x is a palindrome, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversed = 0
        if x < 0:
            return False
        
        if x == 0:
            return True

        temp = x
        while temp > 0:
            temp, remainder = divmod(temp, 10)
            reversed = reversed * 10 + remainder

        return reversed == x 

solution = Solution()

input_1 = 121
print(f"{input_1} is palindrome? {solution.isPalindrome(input_1)}")

input_1 = -121
print(f"{input_1} is palindrome? {solution.isPalindrome(input_1)}")

"""
Time complexity: O(log10N)
- we are diving the input number until is becomes 0
- this requires log10N + 1 operationr
- log10N operation to reach 1
- 1 additional operation of reach 0
hence time complexity is O(log10N+1) ~= O(log10N)

Space Complexity: O(1)
- we are using only two new variables to store x temporarily and reversed number
- there will alaways be just two variables no matter the input
- hence the space complexity is constant. O(1)

"""