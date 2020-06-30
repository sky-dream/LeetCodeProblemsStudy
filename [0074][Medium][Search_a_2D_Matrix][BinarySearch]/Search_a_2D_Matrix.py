# -*- coding: utf-8 -*-  
# solution 1, binary search
# Time  Complexity: O(logN)
# Space Complexity: O(1)
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)     # get row num
        if m == 0:
            return False
        n = len(matrix[0])      # get column num
        
        # 二分查找
        left, right = 0, m * n - 1
        while left <= right:
                pivot_idx = left + (right - left) // 2
                pivot_element = matrix[pivot_idx // n][pivot_idx % n]
                if target == pivot_element:
                    return True
                else:
                    if target < pivot_element:
                        right = pivot_idx - 1
                    else:
                        left = pivot_idx + 1
        return False

def main():
    matrix, target = [[1,3,5,7],[10,11,16,20],[23,30,34,50]],3
    obj = Solution()
    result = obj.searchMatrix(matrix, target)
    assert result == True, ["hint: result is wrong"]
    print("return result is :",result)
    
if __name__ =='__main__':
    main()   