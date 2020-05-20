#-*- coding: utf-8 -*-  
# leetcode time     cost : 52 ms
# leetcode memory   cost : 18.5 MB
# Time  Complexity: O(m*n)
# Space Complexity: O(1)
# solution 1, brute force
class Solution:
    def searchMatrix(self, matrix, target):
        for row in matrix:
            if target in row:
                return True
        
        return False
    
def main():
    inputX_1,inputX_2 = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],5
    expectRes = True
    obj = Solution()
    result = obj.searchMatrix(inputX_1,inputX_2)
    try:
        assert result == expectRes
        print("passed, result is follow expect:",result)
    except AssertionError as aError:
        print('failed, result >> ', result,"<< is wrong, ","expect is : "+ expectRes)
    
if __name__ =='__main__':
    main() 