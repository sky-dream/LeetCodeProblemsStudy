# solution 1 ,dp
class Solution:
    def tribonacci(self, n: int) -> int:
        if n<=1:
            return n
        dp = [0 for i in range(n+1)]
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1  
        for i in range(3,n+1):
            dp[i] =  dp[i-1] + dp[i-2] + dp[i-3]
        return  dp[n]   
    
def main():
    n = 25      #expect is 1389537   
    obj = Solution()
    res = obj.tribonacci(n)
    print("return value is ",res);
    
if __name__ =='__main__':
    main()      