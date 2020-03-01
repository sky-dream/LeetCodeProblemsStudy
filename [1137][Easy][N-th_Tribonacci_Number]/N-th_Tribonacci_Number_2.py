# solution 1 ,dp with memory compress
class Solution:
    def tribonacci(self, n: int) -> int:
        if n<=1:
            return n
        dp = [0 for i in range(n+1)]
        dp_0,dp_1,dp_2 = 0,1,1
        dp_prev_3, dp_prev_2,dp_prev_1 = dp_0,dp_1,dp_2
        dp_i =  dp_2
        for i in range(3,n+1):
            dp_i =  dp_prev_3 + dp_prev_2 + dp_prev_1
            dp_prev_3 = dp_prev_2
            dp_prev_2 = dp_prev_1
            dp_prev_1 = dp_i
        return  dp_i   
    
def main():
    n = 25      #expect is 1389537   
    obj = Solution()
    res = obj.tribonacci(n)
    print("return value is ",res);
    
if __name__ =='__main__':
    main()      