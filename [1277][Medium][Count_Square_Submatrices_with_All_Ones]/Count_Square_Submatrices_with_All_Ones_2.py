# leetcode time     cost : 780 ms
# leetcode memory   cost : 15.6 MB 
# Time  Complexity: O(MN)
# Space Complexity: O(1)
# solution 1, DP, refer to No.221
class Solution:
    def countSquares(self, A):
        for i in range(1, len(A)):
            for j in range(1, len(A[0])):
                A[i][j] *= min(A[i - 1][j], A[i][j - 1], A[i - 1][j - 1]) + 1
        return sum(map(sum, A))

def main():
    matrix = [[0,1,1,1],[1,1,1,1],[0,1,1,1]]  # expect is 15
    Solution_obj = Solution()
    result = Solution_obj.countSquares(matrix)
    print("result value is ",result)
    
if __name__ =='__main__':
    main()  