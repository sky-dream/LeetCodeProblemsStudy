# leetcode time     cost : 44 ms
# leetcode memory   cost : 14.6 MB 
# Time  Complexity: O(n**2)
# Space Complexity: O(n)
# https://leetcode.com/problems/longest-increasing-subsequence/discuss/75012/4-lines-Python-O(n2)
# solution 3, DP, Build a collection of (lastNumber, length) pairs, 4-lines-Python-O(n2),
class Solution(object):
    def lengthOfLIS(self, nums):
        # ends is a list of pair (lastNumber, length), 
        # eg: [(-inf, 0), [1, 1], [3, 2], [6, 3]]
        ends = [(float('-inf'), 0)]
        for a in nums:
            ends += [a, max(m + 1 for b, m in ends if a > b)],
        return  max((zip(*ends))[1])          # max(length for value,length in ends)
    
    def lengthOfLIS_2(self, nums):
        ends = [(float('-inf'), 0)]
        for num in nums:
            ends += (num, max(length + 1
                            for lastNum, length in ends
                            if num > lastNum)),
        return max(list(zip(*ends))[1]) 

def main():
    nums = [1,3,6,7,9,4,10,5,6] #expect is 6
    obj = Solution()
    result = obj.lengthOfLIS(nums)
    print("return result is "+str(result));

if __name__ =='__main__':
    main() 