# -*- coding: utf-8 -*-
# leetcode time     cost : 124 ms
# leetcode memory   cost : 13.8 MB 
# solution 1. Sliding window
# Time  Complexity: O(M+N)
# Space Complexity: O(M+N)
from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or not t:
            return ''
        t_dict = defaultdict(lambda: 0)
        window_dict = defaultdict(lambda: 0)
        for i in t:
            t_dict[i] += 1
        min_len = len(s) + 1
        subStr_Index = [0, 0]
        left, right = 0, 0
        distance = 0
        while right < len(s):
            if window_dict[s[right]] < t_dict[s[right]]:
                distance += 1
            window_dict[s[right]] += 1
            right += 1
            
            while distance == len(t):
                if window_dict[s[left]] > t_dict[s[left]]:
                    window_dict[s[left]] -= 1
                    left += 1
                else:
                    if right - left < min_len:
                        min_len = right - left
                        subStr_Index = [left, right]
                    break
                    
        if min_len == len(s) + 1:
            return ''
        return s[subStr_Index[0]: subStr_Index[1]]

def main():
    s,t = "ADOBECODEBANC","ABC" 
    expect = "BANC"
    obj = Solution()
    result = obj.minWindow(s,t)
    try:
        assert result == expect
        print("passed, result is follow expect:",result)
    except AssertionError as aError:
        print('failed, result is wrong', result, aError.__str__())
    
if __name__ =='__main__':
    main() 