# leetcode time     cost : 236 ms
# leetcode memory   cost : 20.4 MB 
# Time  Complexity: O(N)
# Space Complexity: O(N)
# Segment Tree,线段树
class SegmentTreeNode(object):
    def __init__(self, val, start, end):
        self.val = val
        self.start = start
        self.end = end
        self.children = []


class SegmentTree(object):
    def __init__(self, n):
        self.root = self.build(0, n - 1)

    def build(self, start, end):
        if start > end:
            return

        root = SegmentTreeNode(0, start, end)
        if start == end:
            return root

        mid = start + end >> 1
        # filter()和map()类似，也接收一个函数和一个序列。
        # 和map()不同的时，filter()把传入的函数依次作用于每个元素，
        # 然后根据返回值是True还是False决定保留还是丢弃该元素
        # 递归调用self.build(start, end)
        root.children = filter(None, [
            self.build(start, end)
            for start, end in ((start, mid), (mid + 1, end))])
        return root

    def update(self, i, val, root=None):
        root = root or self.root
        if i < root.start or i > root.end:
            return root.val

        if i == root.start == root.end:
            root.val += val
            return root.val

        root.val = sum([self.update(i, val, c) for c in root.children])
        return root.val

    def sum(self, start, end, root=None):
        root = root or self.root
        if end < root.start or start > root.end:
            return 0

        if start <= root.start and end >= root.end:
            return root.val

        return sum([self.sum(start, end, c) for c in root.children])


class Solution(object):
    def countSmaller(self, nums):
        hashTable = {v: i for i, v in enumerate(sorted(set(nums)))}

        tree, r = SegmentTree(len(hashTable)), []
        for i in range(len(nums) - 1, -1, -1):
            r.append(tree.sum(0, hashTable[nums[i]] - 1))
            tree.update(hashTable[nums[i]], 1)
        return r[::-1]

def main():
    array = [5,2,6,1]      #expect is [2,1,1,0]    
    obj = Solution()
    res = obj.countSmaller(array)
    print("return value sis ",res);
    
if __name__ =='__main__':
    main()