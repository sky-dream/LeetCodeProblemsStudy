# leetcode time     cost : 40 ms
# leetcode memory   cost : 13.6 MB 
# Time  Complexity: O(1)
# Space Complexity: O(1)
# solution 1. record prefix sum
from collections import deque, defaultdict
class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time = deque()
        self.lookup = defaultdict(int)
        self.now = 0

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        while self.time and timestamp - self.time[-1] + 1 > 300:
            self.lookup.pop(self.time.pop())
        if timestamp > self.now:
            self.time.appendleft(timestamp)
            self.now = timestamp
        self.lookup[timestamp] += 1

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        while self.time and timestamp - self.time[-1] + 1 > 300:
            self.lookup.pop(self.time.pop())
        return sum(self.lookup.values())