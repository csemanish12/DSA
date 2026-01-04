class Solution:
    def fibonacci(self, n: int) -> int:
        if n <= 1:
            return n
        
        dp = [-1 for _ in range(n+1)]
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]
    


input_1 = 5
expected_output = 5
actual_output = Solution().fibonacci(input_1)
print(f"expected:{expected_output}, actual:{actual_output}")

input_1 = 7
expected_output = 13
actual_output = Solution().fibonacci(input_1)
print(f"expected:{expected_output}, actual:{actual_output}")

"""
Space complexity: O(n)
Explanation:
- dp array => O(n)
space complexity => O(n)

Time complexity: O(n)
Explanation:
- loop from 2 to n => O(n)
time complexity => O(n)

"""