# leetcode time     cost : 52 ms
# leetcode memory   cost : 13.9 MB
# solution 1, backtracking with swapping elements
# Time  Complexity: O(N*N!)
# Space Complexity: O(N*N!)
# https://leetcode-cn.com/problems/permutations-ii/solution/shuang-bai-si-lu-chao-ji-jian-ji-by-tai-yang-tian/
from typing import List
class Solution(object):
    def permuteUnique(self, nums):
        def backtrack(current_len = 0):
            if current_len == n:  
                res.append(nums[:])
                return
            backtrack(current_len + 1)
            for i in range(0, current_len):
                if(nums[i] == nums[current_len]):
                    return
                nums[current_len], nums[i] = nums[i], nums[current_len]
                backtrack(current_len + 1)
                nums[current_len], nums[i] = nums[i], nums[current_len]
        
        nums.sort()
        n = len(nums)
        res = []
        backtrack()
        return res
def main():
    inputX,expectRes = [1,1,2], [[1,1,2],[1,2,1],[2,1,1]]
    obj = Solution()
    result = obj.permute(inputX)
    try:
        assert result == expectRes
        print("passed, result is follow expect:",result)
    except AssertionError as aError:
        print('failed, result >> ', result,"<< is wrong, ","expect is : "+ expectRes)
    
if __name__ =='__main__':
    main()  