# leetcode time     cost : 40 ms
# leetcode memory   cost : 13.9 MB 
# Time  Complexity: O(M*N)
# Space Complexity: O(M*N)
# solution 1. dp with iteration
# solution 1,DP
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)
        if n1 + n2 != n3: return False

        dp = [[False] * (n2 + 1) for _ in range(n1 + 1)]

        dp[0][0] = True
        # 第一行
        for j in range(1, n2 + 1):
            dp[0][j] = (dp[0][j - 1] and s2[j - 1] == s3[j - 1])

        # 第一列
        for i in range(1, n1 + 1):
            dp[i][0] = (dp[i - 1][0] and s1[i - 1] == s3[i - 1])
        # print(dp)

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (
                        dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
        # print(dp)
        return dp[-1][-1]

def main():
    s1, s2, s3 ="aabcc", "dbbca","aadbbcbcac"          # expect is true,
    obj = Solution()
    result = obj.isInterleave(s1, s2, s3)        
    print("return result is ",result);
    
if __name__ =='__main__':
    main() 