# leetcode time     cost : 24 ms
# leetcode memory   cost : 13.5 MB 
# Time  Complexity: O(N)
# Space Complexity: O(1)
# DP, refer to No.198,select the 1st elememt or not select it.
class Solution:
    def rob(self, nums):
        def rob_198(nums):
            now = prev = 0
            for n in nums:
                now, prev = max(now, prev + n), now
            return now
        return max(rob_198(nums[len(nums) != 1:]), rob_198(nums[:-1]))

def main():
    array = [2,3,2]      #expect is 3   
    obj = Solution()
    res = obj.rob(array)
    print("return value is ",res);
    
if __name__ =='__main__':
    main() 