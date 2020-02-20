#-*- coding: utf-8 -*-  
# leetcode time     cost : 452 ms
# leetcode memory   cost : 53.1 MB 
# Definition for a Trie.
class TrieNode:
    def __init__(self):
        self.one = None
        self.zero = None

# solution analysis, start from the most important bit, the high bit to handle all the nums by bits from high to low.
from collections import deque
class Solution:
    def __init__(self):
        self.root = TrieNode()
        self.maxBit = 31
    
    def insertNumToTrie(self,nums):
        for num in nums:
            node = self.root
            for j in range (self.maxBit, -1, -1):
                tmp = num & 1 << j
                if tmp:
                    if not node.one:
                        node.one = TrieNode()
                    node = node.one
                else:
                    if not node.zero:
                        node.zero = TrieNode()
                    node = node.zero
        return self.root

    def get_max_XOR_FromTrie(self,nums,node):
        maxValue = 0
        for num in nums:
            node = self.root
            tmp_val = 0
            for j in range (31, -1, -1):
                tmp = num & 1 << j
                if node.one and node.zero:
                    if tmp:
                        node = node.zero
                    else:
                        node = node.one
                    tmp_val += 1 << j
                else:
                    if (node.zero and tmp) or (node.one and not tmp):
                        tmp_val += 1 << j
                    node = node.one or node.zero
            maxValue = max(maxValue, tmp_val)
        return maxValue

    def printRoot(self):
        queue = deque([self.root,])
        while queue:
            node = queue.popleft()
            if node and node.zero:    
                queue.append(node.zero)  
                print("printRoot, value zero: ",node.zero) 
            if node and node.one:    
                queue.append(node.one) 
                print("printRoot, value one: ",node.one) 

    def findMaximumXOR(self, nums):
        if not nums: 
            return 0
        self.insertNumToTrie(nums)
        #self.printRoot()
        maxValue = self.get_max_XOR_FromTrie(nums,self.root)
        return maxValue

def main():
    obj = Solution()
    nums = [3,10,5,25,2,8]      # expect is 28
    result = obj.findMaximumXOR(nums)
    print("return result is :",result)
    
if __name__ =='__main__':
    main()  