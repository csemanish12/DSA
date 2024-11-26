def get_nth_fibonacci(n): 
    prev2 = 0
    prev = 1

    if n == 0 or n == 1:
        return n

    for _ in range(2, n+1):
        curr = prev + prev2
        prev2 = prev
        prev = curr

    return prev


nth = 6
print(f"fibonacci number at position {nth} is {get_nth_fibonacci(nth)}")