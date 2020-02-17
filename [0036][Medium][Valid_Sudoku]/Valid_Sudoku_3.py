# solution 1, iteration one time.
# leetcode time     cost : 80 ms
# leetcode memory   cost : 11.8 MB 
# Time  Complexity: O(1)
# Space Complexity: O(1)
# Using len(set).
class Solution:
    def isValidSudoku(self, board):
        seen = sum(( [(c, i), (j, c), (i//3, j//3, c)]
                    for i, row in enumerate(board)
                    for j, c in enumerate(row)
                    if c != '.'), [])
# seen = [('5', 0), (0, '5'), (0, 0, '5'), ('3', 0), (1, '3'), (0, 0, '3'), ('7', 0), (4, '7'), (0, 1, '7'),.......] 
        return len(seen) == len(set(seen))
def main():
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]];
    Solution_obj = Solution()
    result = Solution_obj.isValidSudoku(board);
    print("result value is "+str(result));
    
if __name__ =='__main__':
    main()  