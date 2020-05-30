# -*- coding: utf-8 -*-
# leetcode time     cost : 1868 ms
# leetcode memory   cost : 13.8 MB 
# solution 1. Sliding window
# Time  Complexity: O(M+N)
# Space Complexity: O(M+N)
import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s += '#'  # 向后处理
        maxLen = len(s)  # 因在字符串结尾加上尾巴，最大这么多
        t_cnt = collections.Counter(t)
        window = collections.Counter()
        left = right = 0
        start = end = 0
        
        while right < len(s):
            # 对比频数统计字典，确认window已全部包含t中字符
            if (window & t_cnt) == t_cnt:   # high time cost,
                # right多走了一格
                if right - left < maxLen:
                    maxLen = right - left
                    start, end = left, right
                if window[s[left]] >= 1:
                    window[s[left]] -= 1
                # if window[s[left]] == 1: # 另一种写法
                #     window.pop(s[left])
                # else:
                #     window[s[left]] -= 1
                left += 1
            else:
                # window[s[right]] = window.get(s[right], 0) + 1  # 另一种写法
                window[s[right]] += 1
                right += 1
        return s[start:end]  # end 多走一格

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