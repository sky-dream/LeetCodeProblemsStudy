# leetcode time     cost : 796 ms
# leetcode memory   cost : 18.1 MB 
# Time  Complexity: O(MN)
# Space Complexity: O(1)
# solution 2, DP， from left to right
class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        m = len(s1)
        n = len(s2)
        # 建立二维dp数组并初始化
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            dp[i + 1][0] = dp[i][0] + ord(s1[i])
        for j in range(n):
            dp[0][j + 1] = dp[0][j] + ord(s2[j])
        # print("init_dp: " + str(dp))  

        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j] + ord(s1[i-1]), dp[i][j-1] + ord(s2[j-1]))
        return dp[-1][-1]

def main():  
    s1 = "sea" #expect is 231
    s2 = "eat"   
    obj = Solution()
    result = obj.minimumDeleteSum(s1,s2)
    print("return result is ",result)
    
if __name__ =='__main__':
    main() 