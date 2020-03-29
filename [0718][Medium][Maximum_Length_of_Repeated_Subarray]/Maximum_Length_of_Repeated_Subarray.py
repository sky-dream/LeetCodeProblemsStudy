# leetcode time     cost : 4760 ms
# leetcode memory   cost : 38.9 MB 
# Time  Complexity: O(MN)
# Space Complexity: O(MN)
# solution 1, DP.
class Solution:
    def findLength(self, A: [int], B: [int]) -> int:
        dp=[[0]*(len(B)+1) for _ in range(len(A)+1)]
        res=0
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i]==B[j]:
                    dp[i+1][j+1]=dp[i][j]+1
                    res=max(dp[i+1][j+1],res)
        return res

def main():
    arr1,arr2 = [1,2,3,2,1],[3,2,1,4,7]    #expect is 3
    obj = Solution()
    result = obj.findLength(arr1,arr2)
    print("return result is ",result);

if __name__ =='__main__':
    main() 