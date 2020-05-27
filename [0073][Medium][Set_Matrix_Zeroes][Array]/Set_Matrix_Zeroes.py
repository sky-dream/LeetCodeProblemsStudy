# -*- coding: utf-8 -*-  
# solution 1, 
# Time  Complexity: O(M*N)
# Space Complexity: O(M+N)
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        R = len(matrix)
        C = len(matrix[0])
        rows, cols = set(), set()

        # Essentially, we mark the rows and columns that are to be made zero
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        # Iterate over the array once again and using the rows and cols sets, update the elements
        for i in range(R):
            for j in range(C):
                if i in rows or j in cols:
                    matrix[i][j] = 0 

def main():
    board = [[1,1,1],[1,0,1],[1,1,1]]
    obj = Solution()
    obj.setZeroes(board)
    result = board
    assert result == [[1,0,1],[0,0,0],[1,0,1]], ["hint: result is wrong"]
    print("return result is :",result)
    
if __name__ =='__main__':
    main()   