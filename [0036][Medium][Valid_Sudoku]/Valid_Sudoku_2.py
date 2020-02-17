# solution 1, iteration one time.
# leetcode time     cost : 92 ms
# leetcode memory   cost : 11.8 MB 
# Time  Complexity: O(1)
# Space Complexity: O(1)
# Using Counter. One logical line, seven physical lines.
import collections
class Solution:
    def isValidSudoku(self, board):
        return 1 == max(collections.Counter(
            x
            for i, row in enumerate(board)
            for j, c in enumerate(row)
            if c != '.'
            for x in ((c, i), (j, c), (i//3, j//3, c))
        ).values() + [1])
# i is row, j is column, c is the num char from the input board.
# why (c, j) but (i, c)? (the order of c, j, and i),
# it is aim to distinguish rows and columns, for example ('4', 4) and (4, '4').