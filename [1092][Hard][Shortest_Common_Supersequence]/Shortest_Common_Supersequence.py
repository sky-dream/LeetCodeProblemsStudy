# -*- coding: utf-8 -*-  
# leetcode time     cost : 568 ms
# leetcode memory   cost : 21.5 MB
# Time  Complexity: O(M*N)
# Space Complexity: O(M*N)
# solution 1, DP
class Solution:
        def shortestCommonSupersequence(self,str1:str,str2:str)->str:
            dp=[[0]*(len(str2)+1) for i in range(len(str1)+1)]
            s=''
            max_num=0#用来判断是否两个字符串中有相同子序列
            for i in range(len(str1)):#求最长相同子序列dp
                for j in range(len(str2)):
                    if str1[i]==str2[j]:
                        dp[i+1][j+1]=dp[i][j]+1
                    else:
                        dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])
                    max_num=dp[i+1][j+1]
            i=len(str1)
            j=len(str2)
            if not max_num:#如果没有相同子序列，则返回两个字符串的相加结果
                return str1+str2
            while i!=0 and j!=0:#dp数组回溯，
                if dp[i][j]==dp[i-1][j]:#连续左值相等
                    s+=str1[i-1]
                    i-=1
                elif dp[i][j]==dp[i][j-1]:#连续上值相等
                    s+=str2[j-1]
                    j-=1
                else:
                    j-=1
            for item in range(i-1,-1,-1):#向上扫描完但是向左没有扫描完的情况
                s+=str1[item]

            for item in range(j-1,-1,-1):#向左扫描完但是向上没有扫描完的情况
                s+=str2[item]
            return s[::-1]

def main():
    str1,str2 = "abac","cab"     #expect is "cabac"
    obj = Solution()
    res = obj.shortestCommonSupersequence(str1,str2)
    print("return value is ",res);
    
if __name__ =='__main__':
    main() 