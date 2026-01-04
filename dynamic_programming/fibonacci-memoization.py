class Solution:
    def fibonacci(self, n: int) -> int:
        dp = [-1 for _ in range(n+1)]
        result = self._fibonacci(n, dp)
        return result

    
    def _fibonacci(self, n: int, dp: list[int]) -> int:
        # Base condition
        if n <= 1:
            return n
        
        if dp[n] != -1:
            return dp[n]
        
        result = self._fibonacci(n-1, dp) + self._fibonacci(n-2, dp)
        dp[n] = result

        return result

input_1 = 5
expected_output = 5
actual_output = Solution().fibonacci(input_1)
print(f"expected:{expected_output}, actual:{actual_output}")

input_1 = 900
expected_output = 13
actual_output = Solution().fibonacci(input_1)
print(f"expected:{expected_output}, actual:{actual_output}")

"""
Space complexity: O(n)
Explanation:
- dp array => O(n)
- recursion stack =>  O(n) 
  - Detail: Maximum depth occurs when computing fibonacci(n). Depth is n.
space complexity = O(n) + O(n) => O(n)
  
Time complexity: O(n)
Explanation:
- recursion call => O(n)
  - Details: Each Fibonacci number from 0 to n is computed once due to memoization, so the total number of recursive calls is linear.
time complexity = O(n)
"""