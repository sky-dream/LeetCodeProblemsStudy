# -*- coding: utf-8 -*- 
# leetcode time     cost : 40 ms
# leetcode memory   cost : 14.3 MB 
# Time  Complexity:  O(logN)
# Space Complexity:  O(1)
# solution 1, binary_search
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray:
   def get(self, index: int) -> int:
       pass
   def length(self) -> int:
       pass

def binary_search(mountain, target, l, r, key=lambda x: x):
    target = key(target)
    while l <= r:
        mid = (l + r) // 2
        cur = key(mountain.get(mid))
        if cur == target:
            return mid
        elif cur < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        l, r = 0, mountain_arr.length() - 1
        while l < r:
            mid = (l + r) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                l = mid + 1
            else:
                r = mid
        peak = l
        index = binary_search(mountain_arr, target, 0, peak)
        if index != -1:
            return index
        index = binary_search(mountain_arr, target, peak + 1, mountain_arr.length() - 1, lambda x: -x)
        return index