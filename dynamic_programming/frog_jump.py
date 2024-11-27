"""
There is a frog on the '1st' step of an 'N' stairs long staircase. The frog wants to reach the 'Nth' stair. 'HEIGHT[i]' is the height of the '(i+1)th' stair.If Frog jumps from 'ith' to 'jth' stair, the energy lost in the jump is given by absolute value of ( HEIGHT[i-1] - HEIGHT[j-1] ). If the Frog is on 'ith' staircase, he can jump either to '(i+1)th' stair or to '(i+2)th' stair. Your task is to find the minimum total energy used by the frog to reach from '1st' stair to 'Nth' stair.

For Example
If the given ‘HEIGHT’ array is [10,20,30,10], the answer 20 as the frog can jump from 1st stair to 2nd stair (|20-10| = 10 energy lost) and then a jump from 2nd stair to last stair (|10-20| = 10 energy lost). So, the total energy lost is 20.
Detailed explanation ( Input/output format, Notes, Images )
Constraints:
1 <= T <= 10
1 <= N <= 100000.
1 <= HEIGHTS[i] <= 1000 .

Time limit: 1 sec
Sample Input 1:
2
4
10 20 30 10
3
10 50 10
Sample Output 1:
20
0
Explanation of sample input 1:
For the first test case,
The frog can jump from 1st stair to 2nd stair (|20-10| = 10 energy lost).
Then a jump from the 2nd stair to the last stair (|10-20| = 10 energy lost).
So, the total energy lost is 20 which is the minimum. 
Hence, the answer is 20.

For the second test case:
The frog can jump from 1st stair to 3rd stair (|10-10| = 0 energy lost).
So, the total energy lost is 0 which is the minimum. 
Hence, the answer is 0.
Sample Input 2:
2
8
7 4 4 2 6 6 3 4 
6
4 8 3 10 4 4 
Sample Output 2:
7
2
"""
def min_energy_via_recursion(index, cost):
    if index == 0:
        return 0
    
    left = min_energy_via_recursion(index - 1, cost ) + abs(cost[index] - cost[index-1])
    
    if index > 1:
        right = min_energy_via_recursion(index - 2, cost) + abs(cost[index] - cost[index-2])
        return min(left, right)
    
    return left

def min_energy_via_recursion_with_memoization(index, cost, dp):
    if index == 0:
        return 0
    
    if dp[index] != -1:
        return dp[index]
    
    left = min_energy_via_recursion_with_memoization(index-1, cost, dp) + abs(cost[index] - cost[index-1])

    if index > 1:
        right = min_energy_via_recursion_with_memoization(index-2, cost, dp) + abs(cost[index] - cost[index-2])
        dp[index] = min(left, right)
        return dp[index]
    
    dp[index] = left
    return dp[index]

def min_energy_via_tabulation(cost):
    n = len(cost)
    dp = [-1  for _ in range(n)]
    dp[0] = 0

    for i in range(1, n):
        first_step = dp[i - 1 ] + abs(cost[i] - cost[i-1])
        if i > 1:
            second_step = dp[i-2] + abs(cost[i] - cost[i-2])
            dp[i] = min(first_step, second_step)
        else:
            dp[i] = first_step
    
    return dp[n-1]

def min_energy_without_dp_array(cost):
    n = len(cost)
    prev = 0
    prev2 = 0
    for index in range(1, n):
        first_step = prev  + abs(cost[index] - cost[index-1])
        if index > 1:
            second_step = prev2 + abs(cost[index]- cost[index-2])
            curr = min(first_step, second_step)
        else:
            curr = first_step
        
        prev2 = prev
        prev = curr
    
    return prev


input1 = [30, 10, 60, 10, 60, 50]
index1 = 5
dp1 = [-1 for _ in range(len(input1))]
print("min cost:", min_energy_via_recursion(index1, input1))
print("min cost via memoization:", min_energy_via_recursion_with_memoization(index1, input1, dp1))
print("min cost via tabulation:", min_energy_via_tabulation(input1))
print("min cost without dp:", min_energy_without_dp_array(input1))

input2 = [10, 20, 30, 10]
index2 = 3
dp2 = [-1 for _ in range(len(input2))]
print("min cost:", min_energy_via_recursion(index2, input2))
print("min cost via memoization:", min_energy_via_recursion_with_memoization(index2, input2, dp2))
print("min cost via tabulation:", min_energy_via_tabulation(input2))
print("min cost without dp:", min_energy_without_dp_array(input2))

