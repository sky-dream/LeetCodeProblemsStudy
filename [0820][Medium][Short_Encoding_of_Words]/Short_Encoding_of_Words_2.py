# leetcode time     cost : 212 ms
# leetcode memory   cost : 16.2 MB 
# Time  Complexity: O(N)
# Space Complexity: O(1)
# solution 2,Trie
from functools import reduce
import collections
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = list(set(words)) #remove duplicates
        #Trie is a nested dictionary with nodes created
        # when fetched entries are missing
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()
        # reduce(function, iterable[, initializer])
        # reduce(..., S, trie) is trie[S[0]][S[1]][S[2]][...][S[S.length - 1]]
        nodes = [reduce(dict.__getitem__, word[::-1], trie)
                 for word in words]

        #Add word to the answer if it's node has no neighbors
        return sum(len(word) + 1
                   for i, word in enumerate(words)
                   if len(nodes[i]) == 0)

def main():
    words = ["time", "me", "bell"]      #expect is 10
    obj = Solution()
    res = obj.minimumLengthEncoding(words)
    assert res == 10
    
    
if __name__ =='__main__':
    main() 