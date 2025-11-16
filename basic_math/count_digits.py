"""
Problem Statement: Given an integer N, return the number of digits in N.

                Example 1:
                Input:N = 12345
               
                Output:5
                
                Explanation:  The number 12345 has 5 digits.
                                        
                Example 2:
                Input:N = 7789                
                
                Output: 4
                
                Explanation: The number 7789 has 4 digits.                            

"""

def count_digits(n: int):
    counter = 0
    while n > 0:
        n = n // 10
        counter += 1
    
    return counter

input_1 = 12345
print(f"number of digits for input:{input_1} is", count_digits(input_1))

input_2 = 5
print(f"number of digits for input:{input_2} is", count_digits(input_2))


"""
Complexity analysis:

Space complexity: O(1)
- we are using only one variable which stores int value. 
- this variable will always store a single integer value regardless of the input.
- hence constant space

Time complexity: O(log10N+1)
- the complexity is defined by the number of digits
- in worst case, when N is multiples of 10, the number of digit is LogN+1
- as Log10N means, “How many times do you divide N by 10 to reach 1?” 
     -> we can get this number directly by using math library
- we will divide the number by the number of digit, which is N
- and one additional division to make it 0 to break our loop
- hence Log10N + 1
"""


import math
def count_digits_optimal(n: int):
    if n > 0:
        return int(math.log10(n)) + 1 
    return 1

input_1 = 12345
print(f"number of digits using optimal approach for input:{input_1} is", count_digits_optimal(input_1))

input_2 = 5
print(f"number of digits using optimal approach for input:{input_2} is", count_digits_optimal(input_2))
