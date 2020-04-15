# leetcode time     cost : 5184 ms
# leetcode memory   cost : 13.8 MB 
# Time  Complexity: O(N**3)
# Space Complexity: O(N**2)
# solution 1 DP,
class Solution:
    def minimumMoves(self, arr: [int]):
        # dp[i][j]删除arr[i:j+1](左开右闭)这一段所需要进行的操作次数
        
        # if arr[i]==arr[j]: dp[i][j]=dp[i+1][j-1]
        # else: dp[i][j]=min(dp[i][k]+dp[k+1][j])
        n = len(arr)
        dp=[[float("inf") for _ in range(n)] for _ in range(n)]     
        # start with min length           
        for L in range(n):
            for i in range(0,n-L):
                j = i + L
                if i==j:
                    dp[i][j]=1
                elif arr[i]==arr[j]:
                    if L==1:
                        dp[i][j]=1
                    else:
                        dp[i][j]=dp[i + 1][j - 1]
                
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])
        return dp[0][n-1]

def main():
    array = [1,4,1,1,3,2,3,1]        # expect is 2
    obj = Solution()
    result = obj.minimumMoves(array)
    try:
        assert result==2
        print("passed, result is follow expectation:",result)
    except AssertionError as aeeor:
        print('failed, result is wrong', aeeor.__str__())
    
    
if __name__ =='__main__':
    main() 