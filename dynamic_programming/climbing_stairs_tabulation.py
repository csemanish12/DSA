class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        
        # to reach step 3
        prev1 = 2
        prev2 = 1

        for _ in range(3, n+1):
            current = prev1 + prev2
            prev2 , prev1 = prev1, current
        
        return prev1
        




input1 = 1
expected_output = 1
actual_output = Solution().climbStairs(input1)
print(f"expected:{expected_output}, actual:{actual_output}")

input1 = 2
expected_output = 2
actual_output = Solution().climbStairs(input1)
print(f"expected:{expected_output}, actual:{actual_output}")

input1 = 4
expected_output = 5
actual_output = Solution().climbStairs(input1)
print(f"expected:{expected_output}, actual:{actual_output}")


"""
to reach step n,
we combine the steps to reach n-1 and n-2.
so we start from 1 and reach all the way to n.
we just need to store the data of last 2 steps.
"""