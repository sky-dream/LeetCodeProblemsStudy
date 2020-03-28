# leetcode time     cost : 708 ms
# leetcode memory   cost : 18.2 MB 
# Time  Complexity: O(MN)
# Space Complexity: O(1)
# solution 1, DP， from right to left
class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

        for i in range(len(s1) - 1, -1, -1):
            dp[i][len(s2)] = dp[i+1][len(s2)] + ord(s1[i])
        for j in range(len(s2) - 1, -1, -1):
            dp[len(s1)][j] = dp[len(s1)][j+1] + ord(s2[j])

        for i in range(len(s1) - 1, -1, -1):
            for j in range(len(s2) - 1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = min(dp[i+1][j] + ord(s1[i]),
                                   dp[i][j+1] + ord(s2[j]))

        return dp[0][0]

def main():  
    s1 = "sea" #expect is 231
    s2 = "eat"   
    obj = Solution()
    result = obj.minimumDeleteSum(s1,s2)
    print("return result is ",result)
    
if __name__ =='__main__':
    main() 