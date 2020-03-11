# leetcode time     cost : 64 ms
# leetcode memory   cost : 13.7 MB 
# Time  Complexity: O(NlogN)
# Space Complexity: O(N)
# solution 1, DP.
# https://leetcode-cn.com/problems/delete-and-earn/solution/shan-chu-yu-huo-de-dian-shu-by-leetcode/
import collections
class Solution(object):
    def deleteAndEarn(self, nums):
        countDict = collections.Counter(nums)
        prev = None
        # 对于 nums 中的点数 k，我们记录正确的 avoid 和 using，分别了代表不获取点数 k 和获取点数 k 的情况
        avoid = using = 0
        for k in sorted(countDict):
            if k - 1 != prev:
                avoid, using = max(avoid, using), k * countDict[k] + max(avoid, using)
            else:
                avoid, using = max(avoid, using), k * countDict[k] + avoid
            prev = k
        return max(avoid, using)

def main():
    array = [3,4,2]    #expect is 6
    obj = Solution()
    result = obj.deleteAndEarn(array)
    print("return result is ",result);

if __name__ =='__main__':
    main() 