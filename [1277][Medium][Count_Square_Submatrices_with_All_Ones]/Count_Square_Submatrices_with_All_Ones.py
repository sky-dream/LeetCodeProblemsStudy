# leetcode time     cost : 736 ms
# leetcode memory   cost : 15.4 MB 
# Time  Complexity: O(MN)
# Space Complexity: O(MN)
# solution 1, DP, refer to No.221
class Solution:
    def countSquares(self, matrix: [[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        f = [[0] * n for _ in range(m)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    f[i][j] = matrix[i][j]
                elif matrix[i][j] == 0:
                    f[i][j] = 0
                else:
                    f[i][j] = min(f[i][j - 1], f[i - 1][j], f[i - 1][j - 1]) + 1
                ans += f[i][j]
        return ans

def main():
    matrix = [[0,1,1,1],[1,1,1,1],[0,1,1,1]]  # expect is 15
    Solution_obj = Solution()
    result = Solution_obj.countSquares(matrix)
    print("result value is ",result)
    
if __name__ =='__main__':
    main()  