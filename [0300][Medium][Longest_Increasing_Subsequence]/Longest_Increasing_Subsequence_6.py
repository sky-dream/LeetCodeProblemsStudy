# leetcode time     cost : 44 ms
# leetcode memory   cost : 14.6 MB 
# Time  Complexity: O(n**2)
# Space Complexity: O(n)
# solution 3, DP, Build a collection of (lastNumber, length) pairs, 4-lines-Python-O(n2),
# https://leetcode.com/problems/longest-increasing-subsequence/discuss/75012/4-lines-Python-O(n2)
class Solution(object):
    def lengthOfLIS(self, nums):
        ends = [(float('-inf'), 0)]
        for a in nums:
            ends += (a, max(m + 1 for b, m in ends if a > b)),
        # TypeError: 'zip' object is not subscriptable, need check,
        return max(zip(*ends)[1])
    
    def lengthOfLIS_2(self, nums):
        ends = [(float('-inf'), 0)]
        for num in nums:
            ends += (num, max(length + 1
                            for lastNum, length in ends
                            if num > lastNum)),
        # TypeError: 'zip' object is not subscriptable, need check,
        return max(zip(*ends)[1])

def main():
    nums = [1,3,6,7,9,4,10,5,6] #expect is 6
    obj = Solution()
    result = obj.lengthOfLIS(nums)
    print("return result is "+str(result));

if __name__ =='__main__':
    main() 