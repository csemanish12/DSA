"""
Problem statement
Ninja has to implement a data structure ”TRIE” from scratch. Ninja has to complete some functions.

1) Trie(): Ninja has to initialize the object of this “TRIE” data structure.

2) insert(“WORD”): Ninja has to insert the string “WORD”  into this “TRIE” data structure.

3) countWordsEqualTo(“WORD”): Ninja has to return how many times this “WORD” is present in this “TRIE”.

4) countWordsStartingWith(“PREFIX”): Ninjas have to return how many words are there in this “TRIE” that have the string “PREFIX” as a prefix.

5) erase(“WORD”): Ninja has to delete one occurrence of the string “WORD” from the “TRIE”.
Note:

1. If erase(“WORD”) function is called then it is guaranteed that the “WORD” is present in the “TRIE”.

2. If you are going to use variables with dynamic memory allocation then you need to release the memory associated with them at the end of your solution.
Can you help Ninja implement the "TRIE" data structure?

Detailed explanation ( Input/output format, Notes, Images )
Constraints:
1 <= “T” <= 50
1 <= “N” <= 10000
 “WORD” = {a to z}
1 <= | “WORD” | <= 1000

Where “T” is the number of test cases, “N” denotes how many times the functions(as discussed above) we call, “WORD” denotes the string on which we have to perform all the operations as we discussed above, and | “WORD” | denotes the length of the string “WORD”.

Time limit: 1 sec.
Sample Input 1:
1
5
insert coding
insert ninja
countWordsEqualTo coding
countWordsStartingWith nin
erase coding
Sample Output 1:
1
1   
Explanation of sample input 1:
After insertion of “coding” in “TRIE”:"""

class TrieNode:
    def __init__(self) -> None:
        self.children = [None] * 26
        self.ends_with_count = 0
        self.prefix_count = 0
    
    def get(self, char):
        return self.children[ord(char) - ord('a')]

    def put(self, char, node):
        self.children[ord(char) - ord('a')] = node
    

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for char in word:
            node = curr.get(char)
            if not node:
                node = TrieNode()
                curr.put(char, node)
            
            node.prefix_count += 1
            curr = node
        
        curr.ends_with_count += 1
    
    def countWordsEqualTo(self, word):
        curr = self.root
        for char in word:
            node = curr.get(char)
            if not node:
                return 0
            
            curr = node
        
        return curr.ends_with_count
    
    def countWordsStartingWith(self, word):
        curr = self.root
        for char in word:
            node = curr.get(char)
            if not node:
                return 0
        
            curr = node
        
        return curr.prefix_count
    
    def erase(self, word):
        curr = self.root
        for char in word:
            node = curr.get(char)

            if node.ends_with_count > 0:
                node.ends_with_count -= 1
            
            if node.prefix_count > 0:
                node.prefix_count -= 1

            curr = node


trie = Trie()
trie.insert("samsung")
trie.insert("samsung")
trie.insert("vivo")
trie.erase("vivo")
print("# words equal to 'samsung':", trie.countWordsEqualTo("samsung"))
print("# words starting with 'vi':", trie.countWordsStartingWith("vi"))



