#-*- coding: utf-8 -*-  
# leetcode time     cost : 452 ms
# leetcode memory   cost : 53.1 MB 
# Definition for a Trie.
import time
class TrieNode(object):

    def __init__(self):
        self.word = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.word = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.searchFrom(self.root, word)

    def searchFrom(self, node, word):
        for i in range(len(word)):
            c = word[i]
            if c == '.':
                for k in node.children:
                    if self.searchFrom(node.children[k], word[i+1:]):
                        return True
                return False
            elif c not in node.children:
                return False
            node = node.children[c]
        return node.word

def main():
    obj = WordDictionary()
    operation= ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
    words = [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]           # expect is [null,null,null,null,false,true,true,true]
    for i in range(1,7):
        cmd = 'obj.'+operation[i]+"(%r)" % words[i][0]
        result = eval(cmd)
        localtime = time.asctime( time.localtime(time.time()) )
        print(localtime,result)
    
if __name__ =='__main__':
    main()  