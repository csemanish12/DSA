"""
Problem Statement: Given an integer N, print the following pattern.


Examples:

Example 1:
Input: N = 3
Output: 
* * *
* * *
* * *


Example 2:
Input: N = 6
Output:
* * * * * *
* * * * * *
* * * * * *
* * * * * *
* * * * * *
* * * * * *
"""

def print_pattern(n: int):
    for row in range(n):
        for column in range(n):
            print("*", end=" ")
        print("")
    print("")


input_1 = 3
print_pattern(input_1)

input_2 = 6
print_pattern(input_2)