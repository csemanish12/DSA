"""
Ninja developed a love for arrays and strings so this time his teacher gave him an array of strings, ‘A’ of size ‘N’. Each element of this array is a string. The teacher taught Ninja about prefixes in the past, so he wants to test his knowledge.

A string is called a complete string if every prefix of this string is also present in the array ‘A’. Ninja is challenged to find the longest complete string in the array ‘A’.If there are multiple strings with the same length, return the lexicographically smallest one and if no string exists, return "None".

Note :
String ‘P’ is lexicographically smaller than string ‘Q’, if : 

1. There exists some index ‘i’ such that for all ‘j’ < ‘i’ , ‘P[j] = Q[j]’ and ‘P[i] < Q[i]’. E.g. “ninja” < “noder”.

2. If ‘P’ is a prefix of string ‘Q’, e.g. “code” < “coder”.
Example :
N = 4
A = [ “ab” , “abc” , “a” , “bp” ] 

Explanation : 

Only prefix of the string “a” is “a” which is present in array ‘A’. So, it is one of the possible strings.

Prefixes of the string “ab” are “a” and “ab” both of which are present in array ‘A’. So, it is one of the possible strings.

Prefixes of the string “bp” are “b” and “bp”. “b” is not present in array ‘A’. So, it cannot be a valid string.

Prefixes of the string “abc” are “a”,“ab” and “abc” all of which are present in array ‘A’. So, it is one of the possible strings.

We need to find the maximum length string, so “abc” is the required string.
Detailed explanation ( Input/output format, Notes, Images )
Constraints :
1 <= T <= 10
1 <= N <= 10^5
1 <= A[i].length <= 10^5
A[i] only consists of lowercase english letters.
Sum of A[i].length <= 10^5 over all test cases

Time Limit : 1 sec
Sample Input 1 :
2
6
n ni nin ninj ninja ninga
2
ab bc
Sample Output 1 :
ninja
None
Explanation Of Sample Input 1 :
For test case 1 we have, 

All the prefixes of “ninja” -> “n”, “ni”, “nin”, “ninj” and “ninja” are present in array ‘A’. So, “ninja” is a valid answer whereas for “ninga” , the prefix “ning” is not present in array ‘A’.

So we output “ninja”.

For test case 2 we have, 

The prefixes of “ab” are “a” and “ab”. “a” is not present in array ‘A’. So, “ab” is not a valid answer.

The prefixes of “bc” are “b” and “bc”. “b” is not present in array ‘A’. So, “ab” is not a valid answer.

Since none of the strings is a valid answer we output “None”.
Sample Input 2 :
2
5
g a ak szhkb hy 
4
kez vfj vfjq vfjqo 
Sample Output 2 :
ak
None
"""
from typing import *

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isLeaf = False
    
    def get(self, char):
        return self.children[ord(char) - ord('a')]

    def put(self, char, node):
        self.children[ord(char) - ord('a')] = node

    def setLeaf(self):
        self.isLeaf = True


class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for char in word:
            node = curr.get(char)

            if not node:
                node = TrieNode()
                curr.put(char, node)
            curr = node
        curr.setLeaf()
    
    def hasPrefix(self, word):
        curr = self.root
        for char in word:
            node = curr.get(char)
            if not node:
                return False
            
            curr = node

        return curr.isLeaf

def isValidWord(trie, word)-> bool:
    for index in range(1, len(word)+1):
        prefix = word[0: index]

        if not trie.hasPrefix(prefix):
            return False
    
    return True
        

def completeString(n: int, a: List[str])-> str:
    # insert strings into trie
    trie = Trie()
    for word in a:
        trie.insert(word)
    
    # for each word, check if its valid and get max prefix count
    max_count = 0
    longestPrefix = None
    for word in a:
        if not isValidWord(trie, word):
            continue

        if longestPrefix is None:
            longestPrefix = word
        elif len(word) > len(longestPrefix):
            longestPrefix = word
        elif len(word) == len(longestPrefix):
            longestPrefix =  min(word, longestPrefix)
    
    if longestPrefix is None:
        return "None"

    return longestPrefix    



sample = ["n", "ni", "nin", "ninj", "ninja", "ninga"]
print("ans",completeString(6, sample))  

sample2 = ["ab", "bc"]
print("ans",completeString(2, sample2))  