# -*- coding: utf-8 -*-  
# leetcode time     cost : 668 ms
# leetcode memory   cost : 13.8 MB
# Time  Complexity: O(M*N)
# Space Complexity: O(M*N)
# solution 1, DP
from functools import bisect
class Solution:
    def makeArrayIncreasing(self, arr1: [int], arr2: [int]) -> int:
        # use dict solution to maintain the max value in last step,and op_cnt for current loop index in array1
        # assuming there is a -1 before index 0 in the array1
        N1 = len(arr1)
        N2 = len(arr2)
        arr2.sort()
        solution = {-1:0}
        MAX_CNT = 2001 # max array length is 2000
        for num in arr1:
            new_solution = {}
            for prev_max_num,op_cnt in solution.items():
                # get the possible value can be used in current index of array1
                rc_index = bisect.bisect_right(arr2,prev_max_num)
                if rc_index!= N2:
                    rc_num = arr2[rc_index]
                    # use the min value
                    new_solution[rc_num] = min(new_solution.get(rc_num,MAX_CNT),op_cnt+1)
                if num > prev_max_num:
                    # check use this num,keep the cnt, or replace it with rc_num
                    new_solution[num] = min(new_solution.get(num,MAX_CNT),op_cnt)
            # update solution when all possible value checked in aray2
            solution = new_solution
        if solution:
            return min(solution.values())
        else:
            return -1

def main():
    arr1,arr2 = [1,5,3,6,7],[1,3,2,4]     #expect is 1 
    obj = Solution()
    res = obj.makeArrayIncreasing(arr1,arr2)
    print("return value is ",res);
    
if __name__ =='__main__':
    main() 