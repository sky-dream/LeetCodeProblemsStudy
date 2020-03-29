# leetcode time     cost : 744 ms
# leetcode memory   cost : 21.5 MB 
# solution 1, DP
class Solution:
    def longestCommonSubsequence(self,str1, str2) -> int:
        m, n = len(str1), len(str2)
        # 构建 DP table 和 base case
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # 进行状态转移
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    # 找到一个 lcs 中的字符
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            
        return dp[-1][-1]
    
def main():
    text1,text2 = "abcde", "ace"         # expect is 3
    obj = Solution()
    result = obj.longestCommonSubsequence(text1,text2)
    print("return result is :",result)
    
if __name__ =='__main__':
    main() 