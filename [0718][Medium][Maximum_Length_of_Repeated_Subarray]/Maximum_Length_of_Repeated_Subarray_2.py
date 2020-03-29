# leetcode time     cost : 2676 ms
# leetcode memory   cost : 38.9 MB 
# Time  Complexity: O(MN)
# Space Complexity: O(MN)
# solution 1, DP.
class Solution(object):
    def findLength(self, A, B):
        memo = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        for i in range(len(A) - 1, -1, -1):
            for j in range(len(B) - 1, -1, -1):
                if A[i] == B[j]:
                    memo[i][j] = memo[i+1][j+1]+1
        return max(max(row) for row in memo)

def main():
    arr1,arr2 = [1,2,3,2,1],[3,2,1,4,7]    #expect is 3
    obj = Solution()
    result = obj.findLength(arr1,arr2)
    print("return result is ",result);

if __name__ =='__main__':
    main() 