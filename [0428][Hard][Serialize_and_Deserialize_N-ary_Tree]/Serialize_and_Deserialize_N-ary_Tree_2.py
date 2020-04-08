# -*- coding: utf-8 -*-  
# leetcode time     cost : 100 ms
# leetcode memory   cost : 16.8 MB
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
# solution 2, BFS
class Codec:

    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        from collections import deque
        if not root: return ""  
        queue = deque([root])
        res = []
        while queue:
            node = queue.pop()
            res.append(str(node.val))
            res.append(str(len(node.children)))
            for ch in node.children:
                queue.appendleft(ch)
        return ",".join(res)

    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
       #  print(data)
        from collections import deque
        if not data: return 
        data = iter(data.split(","))
        root = Node(int(next(data)), [])
        queue = deque([[root, int(next(data))]])

        while queue:
            node, num = queue.pop()
            for _ in range(num):
                tmp = int(next(data))
                tmp_num = int(next(data))
                tmp_node = Node(tmp, [])
                node.children.append(tmp_node)
                queue.appendleft([tmp_node, tmp_num])
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))