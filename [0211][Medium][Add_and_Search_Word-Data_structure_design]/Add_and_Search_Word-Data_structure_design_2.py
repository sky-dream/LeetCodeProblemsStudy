#-*- coding: utf-8 -*-  
# leetcode time     cost : 560 ms
# leetcode memory   cost : 45.2 MB 
# Definition for a Trie.
import time
class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False
    
class WordDictionary(object):
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True

    def search(self, word):
        node = self.root
        self.res = False
        self.dfs(node, word)
        return self.res
    
    def dfs(self, node, word):
        if not word:
            if node.isWord:
                self.res = True
            return 
        if word[0] == ".":
            for n in node.children.values():
                self.dfs(n, word[1:])
        else:
            node = node.children.get(word[0])
            if not node:
                return 
            self.dfs(node, word[1:])

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
    
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)