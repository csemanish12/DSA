"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1 for _ in range(n+1)]

        dp[n] = self._climb(n, dp)
        return dp[n]
    
    def _climb(self, n: int, dp: list[int]) -> int:
        if n <= 0:
            return 0
        
        if dp[n] != -1:
            return dp[n]
        
        if n == 1 or n == 2:
            dp[n] = n
            return dp[n]
        
        dp[n] = self._climb(n-1, dp) + self._climb(n-2, dp)

        return dp[n]
    

input1 = 1
expected_output = 1
actual_output = Solution().climbStairs(input1)
print(f"expected:{expected_output}, actual:{actual_output}")

input1 = 2
expected_output = 2
actual_output = Solution().climbStairs(input1)
print(f"expected:{expected_output}, actual:{actual_output}")

input1 = 3
expected_output = 3
actual_output = Solution().climbStairs(input1)
print(f"expected:{expected_output}, actual:{actual_output}")

input1 = 4
expected_output = 5
actual_output = Solution().climbStairs(input1)
print(f"expected:{expected_output}, actual:{actual_output}")


# Reasoning
"""
We start from end (our goal).
We want to reach n (say 5). We start from 5. 
We could have reached to 5 either from 4 (when we took 1 step) or from 3 (when we took 2 steps)
We continue this approach till will reach to end. Similar to factorial.
This ensures we only take path that actually leads to 5. Sort of like back tracking
We are also maintaining a dp array to store already solved paths.
"""

"""
Time complexity: O(n)
- we compute for all way from n till 1 or 2.
- we use dp to eliminate already computed onces.
- so all the steps from n till 1 will be computed exactly once

Space complexity: O(n)
- dp array  of size n => O(n)
- recursion stack space => max depth = n, so O(n)
- total = O(n) + O(n) => O(n)
"""