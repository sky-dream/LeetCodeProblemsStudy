# https://leetcode.com/problems/maximal-square/discuss/61935/6-lines-Visual-Explanation-O(mn)
# leetcode time     cost : 152 ms
# leetcode memory   cost : 14.3 MB 
# using more of Python and some "tricks"
class Solution:
    def maximalSquare(self, A):
        for i, r in enumerate(A):
            r = A[i] = list(map(int, r))
            for j, c in enumerate(r):
                if i * j * c:
                    r[j] = min(A[i-1][j], r[j-1], A[i-1][j-1]) + 1
        return max(map(max, A + [[0]])) ** 2

def main():
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]  # expect is 4
    Solution_obj = Solution()
    result = Solution_obj.maximalSquare(matrix)
    print("result value is ",result)
    
if __name__ =='__main__':
    main()  