# Memoization

Known as the “top-down” dynamic programming, usually the problem is solved in the direction of the main problem to the base cases

## Any recursive solution can be memoized as follows

- create dp[n+1] array and initialize it with -1
- before finding answer to any value(say n), we first check if its exists in the dp array. if so, we return value from dp array
- if answer does not exists, that means we are finding the answer for the first time. In this case, we continue with recursion call but before returning the answer we save the result in dp array

### If there are two recursive calls inside a function, the program will run the first call, finish its execution and then run the second call. Due to this reason, each and every call in the recursive tree will be executed. This gives the recursive code its exponential time complexity. If we can store the values of sub-problems in the first time, then we can simply find its value in constant time whenever we need it. This technique is called Memoization. The cases which are solved again and again in recursion are called overlapping sub-problems


# Tabulation

Known as the “bottom-up '' dynamic programming, usually the problem is solved in the direction of solving the base cases to the main problem

Tabulation is a ‘bottom-up’ approach where we start from the base case and reach the final answer that we want. Tabulation helps in optimizing the solution by preventing additional stack space used during recursion.

## Steps to convert Recursive Solution to Tabulation one.

- Declare a dp[] array of size n+1.
- First initialize the base condition values, i.e i=0 and i=1 of the dp array as 0 and 1 respectively.
- Set an iterative loop that traverses the array( from index 2 to n) and for every index set its value as dp[i-1] + dp[i-2]. 