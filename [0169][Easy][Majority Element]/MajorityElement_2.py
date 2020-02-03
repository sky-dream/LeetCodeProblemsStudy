# solution 2, Hash table
# leetcode time     cost : 176 ms
# leetcode memory   cost : 13.2 MB 
# Time  Complexity: O(N)
# Space Complexity: O(N)
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

# get the max value's key from a dict
# d = {"a":1,"b":2, "c":5}
# solution 1, max(d, key=lambda k: d[k])
# solution 2, max(d, key=d.get)
# solution 3, max(d.items(), key=operator.itemgetter(1))[0], not easy understanding, not recomended,