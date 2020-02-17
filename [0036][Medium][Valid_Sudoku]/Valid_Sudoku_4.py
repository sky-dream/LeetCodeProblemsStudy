# solution 1, iteration one time.
# leetcode time     cost : 76 ms
# leetcode memory   cost : 11.8 MB 
# Time  Complexity: O(1)
# Space Complexity: O(1)
# use 'any'
class Solution:
    def isValidSudoku(self, board):
        seen = set()
        return not any(x in seen or seen.add(x)
                    for i, row in enumerate(board)
                    for j, c in enumerate(row)
                    if c != '.'
                    for x in ((c, i), (j, c), (i//3, j//3, c)))