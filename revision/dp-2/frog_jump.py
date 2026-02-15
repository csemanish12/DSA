class Solution:
    def canCross(self, stones: list[int]) -> bool:
        last_jump = 0
        position = 0
        target = stones[-1]
        dp = {}
        return self._can_cross(position, last_jump, target, dp, set(stones))
    
    def _can_cross(self, position: int, last_jump: int, target: int, dp: dict, stones: set) -> bool:
        if (position, last_jump) in dp:
            return dp[(position, last_jump)]
        
        if position == target:
            dp[(position, last_jump)] = True
            return True
        
        for next_jump in [last_jump - 1, last_jump, last_jump + 1]:
            if next_jump < 1:
                continue

            next_position = next_jump + position
            if next_position not in stones:
                continue

            if self._can_cross(next_position, next_jump, target, dp, stones):
                dp[(next_position, next_jump)] = True
                return True
        
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