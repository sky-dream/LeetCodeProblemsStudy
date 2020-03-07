# https://leetcode.com/problems/maximal-square/discuss/61935/6-lines-Visual-Explanation-O(mn)
# leetcode time     cost : 92 ms
# leetcode memory   cost : 14.2 MB 
# do not overwrite the input matrix but uses two integer lists: 
# s tells the sizes of the squares ending it the current row 
# and p does the same for the previous row.
class Solution:
    def maximalSquare(self, A):
        area = 0
        if A:
            p = [0] * len(A[0])
            for row in A:
                s = list(map(int, row))
                for j, c in enumerate(s[1:], 1):
                    s[j] *= min(p[j-1], p[j], s[j-1]) + 1
                area = max(area, max(s) ** 2)
                p = s
        return area

def main():
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]  # expect is 4
    Solution_obj = Solution()
    result = Solution_obj.maximalSquare(matrix)
    print("result value is ",result)
    
if __name__ =='__main__':
    main()  