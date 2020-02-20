#-*- coding: utf-8 -*-  
# https://leetcode.com/problems/add-and-search-word-data-structure-design/discuss/59576/Tree-solutions-18-20-lines
# leetcode time     cost : 364 ms
# leetcode memory   cost : 39.6 MB 
import time
class WordDictionary:

    def __init__(self):
        self.root = {}
    
    def addWord(self, word):
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node[None] = None

    def search(self, word):
        def find(word, node):
            if not word:
                return None in node
            char, word = word[0], word[1:]
            if char != '.':
                return char in node and find(word, node[char])
            return any(find(word, childNode) for childNode in node.values() if childNode)
        return find(word, self.root)
# An iterative alternative for the search method:
    def search_2(self, word):
            nodes = [self.root]
            for char in word:
                nodes = [childNode
                        for node in nodes
                        for key, childNode in node.items()
                        if char in (key, '.') and childNode]
            return any(None in node for node in nodes)
# another one that's a bit longer but faster:  
    def search_3(self, word):
        nodes = [self.root]
        for char in word:
            nodes = [childNode for node in nodes for childNode in
                     ([node[char]] if char in node else
                      filter(None, node.values()) if char == '.' else [])]
        return any(None in node for node in nodes)      

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