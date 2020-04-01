# leetcode time     cost : 2192 ms 
# leetcode memory   cost : 21.9 MB 
# solution 1, DP
class Solution:
    def dieSimulator(self, n: int, rollMax: [int]) -> int:
        dp = [[[0 for _ in range(16)] for _ in range(7)] for _ in range(n + 1)]
        mod = 10**9 + 7
                
        for i in range(1, n + 1):
            # 投掷的数
            for j in range(1, 7):
                # 第一次投掷
                if i == 1:
                    dp[i][j][1] = 1
                    continue
                
                # 数字 j 连续出现 k 次
                for k in range(2, rollMax[j - 1] + 1):
                    dp[i][j][k] = dp[i - 1][j][k - 1]
                    
                # 前一次投出的数不是 j
                s = 0
                for l in range(1, 7):
                    if l == j:
                        continue
                    for k in range(1, 16):
                        s += dp[i - 1][l][k]
                        s %= mod
                dp[i][j][1] = s
        
        res = 0
        for j in range(1, 7):
            for k in range(1, 16):
                # 求投掷 n 次时所有组合总和
                res += dp[n][j][k]
                res %= mod
                
        return res
    
def main():
    n, rollMax = 2,[1,1,2,2,2,3]         # expect is 34
    obj = Solution()
    result = obj.dieSimulator(n, rollMax)
    print("return result is :",result)
    
if __name__ =='__main__':
    main()