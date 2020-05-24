# -*- coding: utf-8 -*- 
# leetcode time     cost : 72 ms
# leetcode memory   cost : 18.6 MB
# solution 2, counter
# Time  Complexity: O(n*k)
# Space Complexity: O(n*k)
import collections
class Solution:
    def groupAnagrams(self,strs):
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
               
            ans[tuple(count)].append(s)
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