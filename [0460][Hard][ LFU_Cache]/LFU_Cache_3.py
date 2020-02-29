# -*- coding: utf-8 -*-  
# leetcode time     cost : 232 ms
# leetcode memory   cost : 23.1 MB
# Time  Complexity: O(1)
# Space Complexity: O(capacity)
# solution 2, using a dictionary and an ordereddict
from collections import OrderedDict
from collections import defaultdict
class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.keyToValFreq = {} # K: key, V: (val, freq)
        # E.g. { freq 1 : {2 : None, 4 : None, 6: None}, freq 2 : {1 : None, 3 : None, 5 : None} }
        self.freqToKeyValue = defaultdict(OrderedDict) # K: freq, V: {key : None}
        self.capacity = capacity # self.capacity does not change
        self.minFreq = 1 # reset to 1 when new element added

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.keyToValFreq:
            return -1
        val, freq = self.keyToValFreq.pop(key)
        self.freqToKeyValue[freq].pop(key)
        if len(self.freqToKeyValue[freq]) == 0 and freq == self.minFreq:
            self.minFreq = freq + 1
        self.freqToKeyValue[freq + 1][key] = None
        self.keyToValFreq[key] = (val, freq + 1)
        return val
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        # Need to handle edge case of LFU cache capacity = 0.
        if self.capacity <= 0:
            return
        
        if key in self.keyToValFreq:
            self.get(key) # Update the key freq in dict
            self.keyToValFreq[key] = (value, self.keyToValFreq[key][1])
            return
                
        if self.capacity <= len(self.keyToValFreq):
            delKey, _ = self.freqToKeyValue[self.minFreq].popitem(last=False) # pop first
            self.keyToValFreq.pop(delKey)
        
        self.keyToValFreq[key] = (value, 1)
        self.freqToKeyValue[1][key] = None 
        self.minFreq = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)