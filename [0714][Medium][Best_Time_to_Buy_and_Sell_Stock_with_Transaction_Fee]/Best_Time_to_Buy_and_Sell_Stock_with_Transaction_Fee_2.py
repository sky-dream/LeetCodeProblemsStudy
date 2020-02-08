# solution 2, one time traversal of the price list.
# leetcode time     cost : 888 ms
# leetcode memory   cost : 20.1 MB 
# Time  Complexity: O(N)
# Space Complexity: O(1)
class Solution(object):
    def maxProfit(self, prices,fee):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if not prices:
            return 0        
        free , have =  0 , float('-inf')        
        for p in prices:
            free, have = max(free, have + p - fee), max(have, free - p)
        return max(free, have)

def main():  
    nums1 = [5,7,2,7,3,3,5,3,0] #expect is 6 for fee =1
    nums2 = [3,2,6,5,0,3] #expect is 5 for fee =1
    fee = 1    
    obj = Solution()
    result = obj.maxProfit(nums2,fee)
    print("return result is "+str(result));
    
if __name__ =='__main__':
    main() 