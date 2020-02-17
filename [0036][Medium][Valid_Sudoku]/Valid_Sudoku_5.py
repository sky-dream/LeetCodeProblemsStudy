# solution 1, iteration one time.
# leetcode time     cost : 104 ms
# leetcode memory   cost : 11.8 MB 
# Time  Complexity: O(1)
# Space Complexity: O(1)
# Iterating a different way.
class Solution:
    def isValidSudoku(self, board):
        seen = sum(([(c, i), (j, c), (i//3, j//3, c)]
                    for i in range(9) for j in range(9)
                    for c in [board[i][j]] if c != '.'), [])
# seen = [('5', 0), (0, '5'), (0, 0, '5'), ('3', 0), (1, '3'), (0, 0, '3'), ('7', 0), (4, '7'), (0, 1, '7'),.......]        
        return len(seen) == len(set(seen))