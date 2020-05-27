# -*- coding: utf-8 -*-  
# solution 2, special flag to indicate the original "0",
# Time  Complexity: O((M×N)×(M+N))
# Space Complexity: O(1)
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        MODIFIED = -1000000
        R = len(matrix)
        C = len(matrix[0])
        for r in range(R):
            for c in range(C):
                if matrix[r][c] == 0:
                    # We modify the elements in place. Note, we only change the non zeros to MODIFIED
                    for k in range(C):
                        matrix[r][k] = MODIFIED if matrix[r][k] != 0 else 0
                    for k in range(R):
                        matrix[k][c] = MODIFIED if matrix[k][c] != 0 else 0
        for r in range(R):
            for c in range(C):
                # Make a second pass and change all MODIFIED elements to 0 """
                if matrix[r][c] == MODIFIED:
                    matrix[r][c] = 0


def main():
    board = [[1,1,1],[1,0,1],[1,1,1]]
    obj = Solution()
    obj.setZeroes(board)
    result = board
    assert result == [[1,0,1],[0,0,0],[1,0,1]], ["hint: result is wrong"]
    print("return result is :",result)
    
if __name__ =='__main__':
    main()   