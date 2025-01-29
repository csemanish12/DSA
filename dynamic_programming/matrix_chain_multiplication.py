class Solution:
    def matrixMultiplication(self, arr):
        i = 1
        j = len(arr) - 1
        
        return self.getOperations(i, j, arr)
    
    def getOperations(self, i, j, arr):
        if i == j:
            return 0
        min_op = float("inf")
        for k in range(i, j):
            operation = arr[i-1] * arr[k] * arr[j] + self.getOperations(i, k, arr) + self.getOperations(k+1, j, arr)
            min_op = min(min_op, operation)
        
        return min_op

sample = [10, 30, 50]
print("ans:",Solution().matrixMultiplication(sample))