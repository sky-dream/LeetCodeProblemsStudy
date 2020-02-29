# -*- coding: utf-8 -*-  
# leetcode time     cost : 238 ms
# leetcode memory   cost : 23.3 MB
# Time  Complexity: O(1)
# Space Complexity: O(capacity)
# solution 2, using a dictionary and an ordereddict
from collections import defaultdict
from collections import OrderedDict
"""
OrderedDict is a dict + double linked list.
A count2node is a dict of OrderedDict, 
so you can look up like this count2node[count][key] to remove/update the node in O(1), 
or count2node[count].popitem(last=True) to remove the oldest node in O(1).
"""
class Node:
    def __init__(self, key, val, count):
        self.key = key
        self.val = val
        self.count = count
    
class LFUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.key2node = {}
        self.count2node = defaultdict(OrderedDict)
        self.minCount = None
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.key2node:
            return -1
        
        node = self.key2node[key]
        del self.count2node[node.count][key]
        
        # clean memory
        if not self.count2node[node.count]:
            del self.count2node[node.count]
        
        node.count += 1
        self.count2node[node.count][key] = node
        
        # NOTICE check minCount!!!
        if not self.count2node[self.minCount]:
            self.minCount += 1
            
            
        return node.val
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if not self.cap:
            return 
        
        if key in self.key2node:
            self.key2node[key].val = value
            self.get(key) # NOTICE, put makes count+1 too
            return
        
        if len(self.key2node) == self.cap:
            # popitem(last=False) is FIFO, like queue
            # it return key and value!!!
            k, n = self.count2node[self.minCount].popitem(last=False) 
            del self.key2node[k] 
        
        self.count2node[1][key] = self.key2node[key] = Node(key, value, 1)
        self.minCount = 1
        return


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)