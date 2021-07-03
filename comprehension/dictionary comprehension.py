# similar to list comprehension with additional requirement of defining a key
squares = {i: i * i for i in range(10)}
print('squares:', squares)

# we can use if conditional for both key as well as values
# get squares if even else cube
squares_and_cubes = {f"even{i}" if i % 2 == 0 else f"odd{i}": i * i if i % 2 == 0 else i * i * i for i in range(10)}
print('squares and cubes:', squares_and_cubes)
