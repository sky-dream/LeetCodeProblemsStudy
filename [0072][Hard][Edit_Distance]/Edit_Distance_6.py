# leetcode time     cost : 176 ms
# leetcode memory   cost : 17 MB 
# Time  Complexity: O(M*N)
# Space Complexity: O(M*N)
# solution 1. dp with iteration 
class Solution(object):
    #def minDistance(self, word1: str, word2: str) -> int:
    def minDistance(self, word1, word2):
        m, n = len(word1), len(word2)
        dp = [list(range(n+1))]+[[r+1]+[0]*n for r in range(m)]
        for i in range(m):
            for j in range(n):
                dp[i+1][j+1] = dp[i][j] if word1[i]==word2[j] else min(dp[i][j], dp[i+1][j], dp[i][j+1]) + 1
        return dp[m][n]

def main():
    word1 = "horse"          # expect is 3,
    word2 = "ros"
    obj = Solution()
    result = obj.minDistance(word1, word2)        
    print("return result is ",result);
    
if __name__ =='__main__':
    main() 