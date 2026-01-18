class Solution:
    def canCross(self, stones: list[int]) -> bool:
        memo = {}
        target = stones[-1]
        stones_set = set(stones)
        memo[(0,0)] = self._dfs(0, 0, stones_set, target, memo)

        return memo[(0,0)]
    
    def _dfs(self, position: int, last_jump: int, stones: set, target: int, memo: dict):
        if (position, last_jump) in memo:
            return memo[(position, last_jump)]
        
        if position == target:
            memo[(position, last_jump)] = True
            return True
        
        for next_jump in [last_jump-1, last_jump, last_jump+1]:
            if next_jump <= 0:
                continue

            next_position = position + next_jump
            if not next_position in stones:
                continue

            if self._dfs(next_position, next_jump, stones, target, memo):
                memo[(position, last_jump)] = True
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