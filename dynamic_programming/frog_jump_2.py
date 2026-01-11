"""
A frog is crossing a river. The river is divided into some number of units, and at each unit, there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

Given a list of stones positions (in units) in sorted ascending order, determine if the frog can cross the river by landing on the last stone. Initially, the frog is on the first stone and assumes the first jump must be 1 unit.

If the frog's last jump was k units, its next jump must be either k - 1, k, or k + 1 units. The frog can only jump in the forward direction.

 

Example 1:

Input: stones = [0,1,3,5,6,8,12,17]
Output: true
Explanation: The frog can jump to the last stone by jumping 1 unit to the 2nd stone, then 2 units to the 3rd stone, then 2 units to the 4th stone, then 3 units to the 6th stone, 4 units to the 7th stone, and 5 units to the 8th stone.
Example 2:

Input: stones = [0,1,2,3,4,8,9,11]
Output: false
Explanation: There is no way to jump to the last stone as the gap between the 5th and 6th stone is too large.
 

Constraints:

2 <= stones.length <= 2000
0 <= stones[i] <= 231 - 1
stones[0] == 0
stones is sorted in a strictly increasing order.
"""

class Solution:
    def canCross(self, stones: list[int]) -> bool:
        last_jump = 0
        position = 0
        target = stones[-1]
        memo = {}
        stone_set = set(stones)
        return self._canCross(position, last_jump, target, stone_set, memo)

    
    def _canCross(self, position: int, last_jump: int, target: int, stones: set, memo: dict):
        if position == target:
            return True
        
        if (position, last_jump) in memo:
            return memo[(position, last_jump)]
        
        for next_jump in [last_jump - 1 , last_jump, last_jump + 1]:
            if next_jump <= 0:
                continue
            
            next_position = position + next_jump

            if next_position not in stones:
                continue

            if self._canCross(next_position, next_jump, target, stones, memo):
                memo[(position,last_jump)] = True
                return True
        
        memo[(position, last_jump)] = False
        return False



input1 = [0,1,3,5,6,8,12,17]
expected_output = True
actual_output = Solution().canCross(input1)
print(f"expected:{expected_output}, actual:{actual_output}")

input1 = [0,1,2,3,4,8,9,11]
expected_output = False
actual_output = Solution().canCross(input1)
print(f"expected:{expected_output}, actual:{actual_output}")

input1 = [0,1,3,6,7]
expected_output = False
actual_output = Solution().canCross(input1)
print(f"expected:{expected_output}, actual:{actual_output}")

input1 = [0,2]
expected_output = False
actual_output = Solution().canCross(input1)
print(f"expected:{expected_output}, actual:{actual_output}")



input1 = [0,1,3,6,10,13,15,18]
expected_output = True
actual_output = Solution().canCross(input1)
print(f"expected:{expected_output}, actual:{actual_output}")


"""
Time Complexity: O(n²) where n is the number of stones

Each stone can be visited with different jump sizes
Maximum jump size is roughly n (in worst case)
Memoization ensures each (position, jump_size) state is computed once


Space Complexity: O(n²)

Memo dictionary can store up to O(n²) states
Recursion stack depth is O(n)
Stone set is O(n)
"""