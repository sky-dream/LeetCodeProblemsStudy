# -*- coding: utf-8 -*-  
# leetcode time     cost : 1008 ms
# leetcode memory   cost : 13.5 MB
# solution 2，中心扩散法，要注意奇数及偶数长度回文
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        for i in range(len(s)):
            res = max(self.helper(s,i,i), self.helper(s,i,i+1), res, key=len)
        return res
       
    def helper(self,s,l,r):        
        while 0<=l and r < len(s) and s[l]==s[r]:
                l-=1; r+=1
        return s[l+1:r]

def main():
    inputX,expectRes = "babad","aba" # ans is "aba" or "bab"
    obj = Solution()
    result = obj.longestPalindrome(inputX)
    try:
        assert result == expectRes
        print("passed, result is follow expect:",result)
    except AssertionError as aError:
        print('failed, result >> ', result,"<< is wrong, ","expect is : "+ expectRes)
    
if __name__ =='__main__':
    main() 