class Solution:
     
    def _binary_search(self, start_index, end_index, target, elements) -> int:
        mid = (start_index + end_index) // 2

        while start_index <= end_index:
            if  elements[mid] == target:
                return mid
            elif elements[mid] < target:
                start_index = mid + 1
            else:
                end_index = mid - 1
            
            mid = (start_index + end_index) // 2
        
        return -1
    

input = [1,2,5,6,9,12]
target = 1
v = Solution()._binary_search(0, len(input) -1, target, input)
print("v", v)