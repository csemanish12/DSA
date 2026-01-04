## Any recursive solution can be converted to DP as follows

- create dp[n+1] array and initialize it with -1
- before finding answer to any value(say n), we first check if its exists in the dp array. if so, we return value from dp array
- if answer does not exists, that means we are finding the answer for the first time. In this case, we continue with recursion call but before returning the answer we save the result in dp array

### If there are two recursive calls inside a function, the program will run the first call, finish its execution and then run the second call. Due to this reason, each and every call in the recursive tree will be executed. This gives the recursive code its exponential time complexity. If we can store the values of sub-problems in the first time, then we can simply find its value in constant time whenever we need it. This technique is called Memoization. The cases which are solved again and again in recursion are called overlapping sub-problems