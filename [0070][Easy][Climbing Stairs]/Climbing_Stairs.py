class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        all_ways_cache = {}
        return self.helper(n, all_ways_cache)
    def helper(self,n, all_ways_cache_dict):        
        if n<=2:
            return n
        if n in all_ways_cache_dict.keys():
            return all_ways_cache_dict[n]
        else:
            all_ways_cache_dict[n] = self.helper(n-1, all_ways_cache_dict) + self.helper(n-2, all_ways_cache_dict)
            return all_ways_cache_dict[n] 
s = Solution()
print(s.climbStairs(30))