"""
You are given an integer n. You need to check whether it is an armstrong number or not. Return true if it is an armstrong number, otherwise return false.



An armstrong number is a number which is equal to the sum of the digits of the number, raised to the power of the number of digits.


Examples:
Input: n = 153

Output: true

Explanation: Number of digits : 3.

13 + 53 + 33 = 1 + 125 + 27 = 153.

Therefore, it is an Armstrong number.

Input: n = 12

Output: false

Explanation: Number of digits : 2.

12 + 22 = 1 + 4 = 5.

Therefore, it is not an Armstrong number.
"""
class Solution:
    def isArmstrong(self, n: int) -> bool:
        length, numbers = self.get_length_and_numbers(n)
        total_sum = 0
        for num in numbers:
            total_sum += num ** length

        return total_sum == n

    
    def get_length_and_numbers(self, n: int) -> int:
        length = 0
        numbers = []
        while n > 0:
            n, remainder = divmod(n, 10)
            length += 1
            numbers.append(remainder)
        
        return length, numbers
    
class SolutionPythonic:
    """
    string conversion is faster and optimized in python instead of modulo
    """
    def isArmstrong(self, n: int) -> bool:
        n_str = str(n)
        length = len(n_str)
        total_result = 0
        for num in n_str:
            total_result += int(num) ** length
        
        return total_result == n
    

class SolutionSpaceOptimized:
    """
    don't store digits in number. Use multiple loops instead.
    first loop to count digit
    second loop to sum the digit
    """
    def isArmstrong(self, n: int) -> bool:
        temp, length = n, 0
        while temp > 0:
            temp = temp // 10
            length += 1
        
        temp, total_sum = n, 0
        while temp > 0:
            temp, rem = divmod(temp, 10)
            total_sum += rem ** length
        
        return total_sum == n

    

input_1 = 153
print("is armstrong via default solution: ", Solution().isArmstrong(input_1))
print("is armstrong via default solutionPythonic: ", SolutionPythonic().isArmstrong(input_1))
print("is armstrong via default SolutionSpaceOptimized: ", SolutionSpaceOptimized().isArmstrong(input_1))