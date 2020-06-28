# leetcode time     cost : 36 ms
# leetcode memory   cost : 13.8 MB
# Time  Complexity: O(n*n!)
# Space Complexity: O(n)
# solution 1,backtracking
from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def trackBack(nums,track):
            if len(track) == len(nums):
                res.append(track[:]) # 需要传递下track的拷贝，否则对track的修改会影响到结果
                return
            for i in nums:
                if i in track:
                    continue
                track.append(i)
                trackBack(nums,track)
                track.pop()
        res = []
        track = []
        trackBack(nums,track)
        return res
def main():
    inputX,expectRes = [1,2,3], [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,2,1],[3,1,2]]
    obj = Solution()
    result = obj.permute(inputX)
    try:
        assert result == expectRes
        print("passed, result is follow expect:",result)
    except AssertionError as aError:
        print('failed, result >> ', result,"<< is wrong, ","expect is : "+ expectRes)
    
if __name__ =='__main__':
    main()  