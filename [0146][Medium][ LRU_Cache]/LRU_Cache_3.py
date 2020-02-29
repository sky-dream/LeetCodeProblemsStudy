# -*- coding: utf-8 -*-  
# leetcode time     cost : 192 ms
# leetcode memory   cost : 21.8 MB
# Time  Complexity: O(1)
# Space Complexity: O(capacity)
# solution 1, ordered dict()
import collections
class LRUCache():

    def __init__(self, capacity):
        self.dict = collections.OrderedDict()
        self.remain = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dict:
            return - 1
        value = self.dict.pop(key)
        self.dict[key] = value # set value as the newest element,
        return self[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.dict:
            self.dict.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1
            else:   # self.dict is full
                self.dict.popitem(last = False)
        self.dict[key] = value

# LRUCache object will be instantiated or called as below:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)