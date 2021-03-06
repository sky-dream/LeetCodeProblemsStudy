#-*- coding: utf-8 -*-  
# Definition for a Trie.
# https://leetcode-cn.com/problems/implement-trie-prefix-tree/solution/pythonjian-dan-shi-xian-by-powcai/
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # self element is a dict, key is the string char, value is the next trie object.
        # use special key # and value # as the ending flag. 
        self.lookup = {}
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        tree = self.lookup
        for a in word:
            if a not in tree:
                tree[a] = {}
            tree = tree[a]
        # 单词结束标志
        tree["#"] = "#"
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tree = self.lookup
        for a in word:
            if a not in tree:
                return False
            # else get the next node by the current char as the key
            tree = tree[a]
        # check the ending flag if all the char in the word already checked.
        if "#" in tree:
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tree = self.lookup
        for a in prefix:
            if a not in tree:
                return False
            tree = tree[a]
        return True