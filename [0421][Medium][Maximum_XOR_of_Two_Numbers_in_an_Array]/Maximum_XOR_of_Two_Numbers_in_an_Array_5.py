#-*- coding: utf-8 -*-  
# leetcode time     cost : 1384 ms
# leetcode memory   cost : 167.3 MB 
'''
Insert the binary representation of a number into the trie. 
Here, we insert from most significant bit to least significant bit, 
meaning the first node in the trie is the MSB and so on..

Everytime we insert a number (let's call this number A), we want to traverse the trie a second time 
and go the opposite way as A's binary representation as much as possible. 
It's important that our trie elements were entered from MSB to LSB 
because this will maximize the differences as we traverse down the tree.

Find the node that diverges most with A and then return the XOR of these two numbers so we can update the max XOR.
'''
class Trie:
    
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word, val):
        curr = self.root
        for i in range(len(word)):
            bit = word[i]
            if bit not in curr.children:
                curr.children[bit] = TrieNode()
            curr = curr.children[bit]
        curr.isEnd = True
        curr.value = val
    
    def search(self, word, target):
        curr = self.root
        for i in range(len(word)):
            bit = word[i]
            
            if bit == '1' and curr.children.get('0'):
                curr = curr.children['0']
            elif bit == '0' and curr.children.get('1'):
                curr = curr.children['1']
            elif curr.children.get(bit):
                curr = curr.children[bit]
            else:
                break
                
        return target^curr.value
            
            
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.value = 0
    

class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.trie = Trie()
        max_xor = -2**(32)
        
        for i in nums:
            binary_string = (bin(i)[2:]).zfill(31)
            self.trie.insert(binary_string, i)
            max_xor = max(max_xor, self.trie.search(binary_string, i))
        
        return max_xor

def main():
    obj = Solution()
    nums = [3,10,5,25,2,8]      # expect is 28
    result = obj.findMaximumXOR(nums)
    print(result)
    
if __name__ =='__main__':
    main()  