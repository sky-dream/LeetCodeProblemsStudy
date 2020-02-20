#-*- coding: utf-8 -*-  
# Easy to read length based set solution.
# leetcode time     cost : 252 ms, time is less is due to the stored data is not big
# leetcode memory   cost : 36.4 MB 
import time
from collections import defaultdict
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words = defaultdict(set)
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.words[len(word)].add(word)
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        for other in self.words[len(word)]:
            any_mismatch = any(word[x] != '.' and word[x] != other[x] for x in range(len(word)))
            if not any_mismatch:
                return True
        return False
    
    
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