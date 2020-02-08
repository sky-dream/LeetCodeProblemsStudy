# solution 2, with hash table
# leetcode time     cost : 436 ms
# leetcode memory   cost : 13.5 MB 
# Time  Complexity: O(time)
# Space Complexity: O(1)
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        c = collections.defaultdict(int)
        for t in tasks:
            c[t] += 1
        m = max(c.itervalues())
        l = len([k for k in c if c[k] == m])
        return max(len(tasks), (m - 1) * (n + 1) + l)