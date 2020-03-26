# leetcode time     cost : 384 ms
# leetcode memory   cost : 17.3 MB 
# Time  Complexity: O(MN)
# Space Complexity: O(MN)
# solution 1, DP,
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        if not n1:
            return n2
        if not n2:
            return n1            
        dp = [ [0]*(n2+1) for _ in range(n1+1)]
        for i in range(n1+1):
            dp[i][0] =  i
        for j in range(n2+1):
            dp[0][j] =  j
        for i in range(1,n1+1):
            for j in range(1,n2+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j]+1,dp[i][j-1]+1)
        return dp[n1][n2]
    
def main():
    word1,word2 = "aeaswqsdaf","befdswerw"  # ans 13
    obj = Solution()
    res = obj.minDistance(word1,word2)
    print("return value is ",res)
    
if __name__ =='__main__':
    main()     