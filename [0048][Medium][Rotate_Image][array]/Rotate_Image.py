# -*- coding: utf-8 -*- 
# leetcode time     cost : 36 ms
# leetcode memory   cost : 13.5 MB
# Time  Complexity: O(n*n)
# Space Complexity: O(1)
# solution 1, transpose and reverse
class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])        
        # transpose matrix
        for i in range(n):
            for j in range(i, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i] 
        
        # reverse each row
        for i in range(n):
            matrix[i].reverse()
            
def main():
    inputX,expectRes = [[1,2,3],[4,5,6],[7,8,9]], [[7,4,1],[8,5,2],[9,6,3]]
    obj = Solution()
    obj.rotate(inputX)
    result = inputX
    try:
        assert result == expectRes
        print("passed, result is follow expect:",result)
    except AssertionError as aError:
        print('failed, result >> ', result,"<< is wrong, ","expect is : ",expectRes)
    
if __name__ =='__main__':
    main()  