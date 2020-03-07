# https://leetcode.com/problems/maximal-square/discuss/61935/6-lines-Visual-Explanation-O(mn)
# leetcode time     cost : 88 ms
# leetcode memory   cost : 14.3 MB 
class Solution:
    def maximalSquare(self, A):
        for i in range(len(A)):
            for j in range(len(A[i])):
                A[i][j] = int(A[i][j])
                if A[i][j] and i and j:
                    A[i][j] = min(A[i-1][j], A[i-1][j-1], A[i][j-1]) + 1
        return len(A) and max(map(max, A)) ** 2

def main():
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]  # expect is 4
    Solution_obj = Solution()
    result = Solution_obj.maximalSquare(matrix)
    print("result value is ",result)
    
if __name__ =='__main__':
    main()  