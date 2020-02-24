# leetcode time     cost : 44 ms
# leetcode memory   cost : 14.6 MB 
# Time  Complexity: O(n**2)
# Space Complexity: O(n)
# solution 4,DP and binarySearch,
# https://leetcode.com/problems/longest-increasing-subsequence/discuss/74824/JavaPython-Binary-search-O(nlogn)-time-with-explanation
# https://leetcode.com/problems/longest-increasing-subsequence/discuss/412340/python-O(N*logN)
import bisect
class Solution(object):
    def lengthOfLIS(self, nums):
        tails = []
        for num in nums:
            i = bisect.bisect_left(tails, num)
            if i == len(tails):
                tails.append(num)
            tails[i] = num
        return len(tails)
    
    def lengthOfLIS_2(self, nums):
            if len(nums)==0: return 0
            
            tails=[]
            for target in nums:
                index=self.binarySearch(tails,target)
                length=index+1
                if length>len(tails):
                    tails.append(target)
                else:
                    tails[index]=target
            return len(tails)
    
    def binarySearch(self,nums,target):
        if len(nums)==0: return 0
        left=0
        right=len(nums)-1
        while True:
            if right-left<=1:break
            mid=(left+right)//2
            if target>nums[mid]:
                left=mid
            else:
                right=mid
        
        if target>nums[right]: return right+1
        elif nums[left]<target<=nums[right]: return right
        else: return left 

def main():
    nums = [1,3,6,7,9,4,10,5,6] #expect is 6
    obj = Solution()
    result = obj.lengthOfLIS(nums)
    print("return result is "+str(result));

if __name__ =='__main__':
    main() 