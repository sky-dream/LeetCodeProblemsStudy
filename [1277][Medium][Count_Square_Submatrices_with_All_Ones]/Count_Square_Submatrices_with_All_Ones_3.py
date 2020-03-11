# leetcode time     cost : 1012 ms
# leetcode memory   cost : 15.5 MB 
# Time  Complexity: O(MN)
# Space Complexity: O(1)
# solution 1, DP, refer to No.221
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    continue
                if i == 0 or j == 0:
                    res += 1
                else:
                    matrix[i][j] = min(min(matrix[i][j-1], matrix[i-1][j]), matrix[i-1][j-1])+1
                    res += matrix[i][j]
        return res

def main():
    matrix = [[0,1,1,1],[1,1,1,1],[0,1,1,1]]  # expect is 15
    Solution_obj = Solution()
    result = Solution_obj.countSquares(matrix)
    print("result value is ",result)
    
if __name__ =='__main__':
    main()  