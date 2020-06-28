# leetcode time     cost : 48 ms
# leetcode memory   cost : 13.9 MB
# Time  Complexity: O(n*n!)
# Space Complexity: O(n*n!)
# solution 1,backtracking with swapping elements
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
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