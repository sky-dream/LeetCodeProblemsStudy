# -*- coding: utf-8 -*- 
# leetcode time     cost : 72 ms
# leetcode memory   cost : 16.7 MB
# Time  Complexity: O(n*k*logK)
# Space Complexity: O(n*k)
# solution 1,sort
import collections
class Solution(object):
    def groupAnagrams(self, strs):
        ans = collections.defaultdict()
        for s in strs:
            if tuple(sorted(s)) not in ans.keys():
                ans[tuple(sorted(s))] = []
            ans[tuple(sorted(s))].append(s)
        return list(ans.values())
            
def main():
    inputX,expectRes = ["eat","tea","tan","ate","nat","bat"], [["eat","tea","ate"],["tan","nat"],["bat"]]
    obj = Solution()
    
    result = obj.groupAnagrams(inputX)
    try:
        assert result == expectRes
        print("passed, result is follow expect:",result)
    except AssertionError as aError:
        print('failed, result >> ', result,"<< is wrong, ","expect is : ",expectRes)
    
if __name__ =='__main__':
    main()  