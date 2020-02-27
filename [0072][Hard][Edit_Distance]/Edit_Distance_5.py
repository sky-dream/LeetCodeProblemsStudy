# leetcode time     cost : 176 ms
# leetcode memory   cost : 13.6 MB 
# Time  Complexity: O(M*N)
# Space Complexity: O(M*N)
# solution 1. dp status compress with iteration 
class Solution(object):
    #def minDistance(self, word1: str, word2: str) -> int:
    def minDistance(self, word1, word2):
        l1, l2 = len(word1)+1, len(word2)+1
        dp = [j for j in range(l2)]
        for i in range(1, l1):
            pre, dp[0] = i-1, i
            for j in range(1, l2):
                buf = dp[j]
                dp[j] = min(dp[j]+1, dp[j-1]+1, pre+(word1[i-1]!=word2[j-1]))
                pre = buf
        return dp[-1]

def main():
    word1 = "horse"          # expect is 3,
    word2 = "ros"
    obj = Solution()
    result = obj.minDistance(word1, word2)        
    print("return result is ",result);
    
if __name__ =='__main__':
    main() 