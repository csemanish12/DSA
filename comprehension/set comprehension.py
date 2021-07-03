# A set comprehension is almost exactly the same as list comprehension.
# The difference is that set comprehension make sure the output contains
# no duplicate.

quote = "life, uh, finds a way"
unique_vowels = {i for i in quote if i in "aeiou"}
print('unique vowels:', unique_vowels)

# capitalize vowels and leave consonant as it is
vowels_and_constants = [i.upper() if i in "aeiou" else i for i in quote if i.isalpha()]
print('vowels and consonant:', vowels_and_constants)