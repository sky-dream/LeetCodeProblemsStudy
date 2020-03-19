# leetcode time     cost : 236 ms
# leetcode memory   cost : 20.4 MB 
# Time  Complexity: O(N)
# Space Complexity: O(N)
# Binary Indexed Tree,树状数组
""" 
tree_8 = tree_4 + tree_6 + tree_7 + num_8
tree_4 = tree_2 + tree_3 + num_4
tree_6 = tree_5 + num_6
tree_7 = num_7
tree_2 = tree_1 + num_2
tree_3 = num_3
tree_5 = num_5
tree_1 = num_1  
"""
class BinaryIndexedTree(object):
    def __init__(self, n):
        self.sums = [0] * (n + 1)
    
    # 由子节点向上修改tree的信息，本例及num[i]右边比自身小的元素个数
    def update(self, i, val):
        while i < len(self.sums):
            self.sums[i] += 1
            i += i & -i
    
    # 由父节点向下查询
    def sum(self, i):
        r = 0
        while i > 0:
            r += self.sums[i]
            i -= i & -i
        return r


class Solution(object):
    def countSmaller(self, nums):
        # 根据num数值v从小到大排列出 {v: i}的字典
        hashTable = {v: i for i, v in enumerate(sorted(set(nums)))}
        # 构建以 num数值 为索引， 元素出现次数为value 的 树状数组
        tree, r = BinaryIndexedTree(len(hashTable)), []
        #从右向左遍历nums,查询Tree中比自己小的元素个数，并把自己加入Tree
        for i in range(len(nums) - 1, -1, -1):
            r.append(tree.sum(hashTable[nums[i]]))
            
            tree.update(hashTable[nums[i]] + 1, 1)
        return r[::-1]