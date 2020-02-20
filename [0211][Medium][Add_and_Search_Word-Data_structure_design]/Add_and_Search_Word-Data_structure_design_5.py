#-*- coding: utf-8 -*-  
# Python-trie-with-defaultdict-trick
# leetcode time     cost : 444 ms
# leetcode memory   cost : 41.4 MB 
import time
from collections import defaultdict

def _trie():
    return defaultdict(_trie)

TERMINAL = None

class WordDictionary(object):
    def __init__(self):
        self.trie = _trie()

    def addWord(self, word):
        trie = self.trie
        for letter in word:
            trie = trie[letter]
        trie[TERMINAL]

    def search(self, word, trie=None):
        if trie is None:
            trie = self.trie
        for i, letter in enumerate(word):
            if letter == '.':
                return any(self.search(word[i+1:], t) for t in trie.values())
            if letter in trie:
                trie = trie[letter]
            else:
                return False
        return TERMINAL in trie
    
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