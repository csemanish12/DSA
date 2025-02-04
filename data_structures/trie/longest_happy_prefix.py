class TrieNode:
    def __init__(self) -> None:
        self.children = [None] * 26
        self.isLeaf = False
    
    def get(self, char):
        return self.children[ord(char) -  ord('a')]
    
    def put(self, char, node):
        self.children[ord(char) -  ord('a')] = node
    
    def setLeaf(self):
        self.isLeaf = True

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

class Solution:
    def longestPrefix(self, s: str) -> str:
        trie = Trie()
        happy_prefix = ""
        # insert prefix
        length = len(s)
        for index in range(1, len(s)):
            prefix = s[0: index]
            trie.insert(prefix)

        # check if suffix matches
        # abcd
        # 0123
        for index in range(1, length):
            prefix = s[index:length]
            if trie.hasPrefix(prefix):
                return prefix
        
        return happy_prefix

sample1 = "ababab"
print("ans:", Solution().longestPrefix(sample1))

sample2 = "level"
print("ans:", Solution().longestPrefix(sample2))