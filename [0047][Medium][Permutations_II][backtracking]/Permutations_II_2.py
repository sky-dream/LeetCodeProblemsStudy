# leetcode time     cost : 40 ms
# leetcode memory   cost : 13.8 MB
# solution 1, backtracking with used notation
# Time  Complexity: O(N*N!)
# Space Complexity: O(N*N!)
# https://leetcode-cn.com/problems/permutations-ii/solution/hui-su-suan-fa-python-dai-ma-java-dai-ma-by-liwe-2/
from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        def dfs(nums, size, depth, path, used, res):
            if depth == size:
                res.append(path.copy())
                return
            for i in range(size):
                if not used[i]:

                    if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                        continue

                    used[i] = True
                    path.append(nums[i])
                    dfs(nums, size, depth + 1, path, used, res)
                    used[i] = False
                    path.pop()

        size = len(nums)
        if size == 0:
            return []

        nums.sort()

        used = [False] * len(nums)
        res = []
        dfs(nums, size, 0, [], used, res)
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