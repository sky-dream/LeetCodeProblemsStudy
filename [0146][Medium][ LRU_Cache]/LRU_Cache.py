# -*- coding: utf-8 -*-  
# leetcode time     cost : 192 ms
# leetcode memory   cost : 21.8 MB
# Time  Complexity: O(1)
# Space Complexity: O(capacity)
# solution 1, ordered dict()
from collections import OrderedDict
class LRUCache(OrderedDict):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self:
            return - 1
        
        self.move_to_end(key)
        return self[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last = False)

# LRUCache object will be instantiated or called as below:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)