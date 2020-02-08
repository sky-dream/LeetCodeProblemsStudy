# solution 2, hash table
# leetcode time     cost : 436 ms
# leetcode memory   cost : 13.5 MB 
# Time  Complexity: O(time)
# Space Complexity: O(1)
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        v = list(collections.Counter(tasks).values())
        # v = map(tasks.count, set(tasks))
        return max((max(v)-1) * (n+1) + v.count(max(v)), len(tasks))