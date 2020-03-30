# leetcode time     cost : 640 ms
# leetcode memory   cost : 13.7 MB 
# solution 1, DP
class Solution:
    def maxSumAfterPartitioning(self, A, K) :
            n=len(A)
            dp=[0]*(n+1)
            for i in range(1,n+1) :
                j=i-1
                domain_max = float("-inf")
                while i-j <= K and j >= 0 :
                    #包含A[j] 的 last domain 所有可能，取最大的
                    domain_max = max(domain_max, A[j])
                    dp[i] = max(dp[i], dp[j] + domain_max *(i-j)) 
                    j-=1
            return dp[n]
    
def main():
    A, K = [1,15,7,9,2,5,10], 3         # expect is 84
    obj = Solution()
    result = obj.maxSumAfterPartitioning(A, K)
    print("return result is :",result)
    
if __name__ =='__main__':
    main() 