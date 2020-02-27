# leetcode time     cost : 180 ms
# leetcode memory   cost : 16.9 MB 
# Time  Complexity: O(M*N)
# Space Complexity: O(M*N)
# solution 1. dp with iteration
class Solution:
    #def minDistance(self, word1: str, word2: str) -> int:
    def minDistance(self, word1, word2):
        m = len(word1)
        n = len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # 第一行
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j-1] + 1
        # 第一列
        for i in range(1, m + 1):
            dp[i][0] = dp[i-1][0] + 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1] ) + 1
        return dp[-1][-1]

def main():
    word1 = "horse"          # expect is 3,
    word2 = "ros"
    obj = Solution()
    result = obj.minDistance(word1, word2)        
    print("return result is ",result);
    
if __name__ =='__main__':
    main() 