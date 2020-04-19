# leetcode time     cost : 56 ms
# leetcode memory   cost : 13.7 MB 
# Time  Complexity: O(1)
# Space Complexity: O(1)
# solutioin 2, add time stamp to queue, count the length of the queue
from collections import deque
class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque()

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.queue.appendleft(timestamp)

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        while self.queue and timestamp - self.queue[-1] + 1 > 300:
            self.queue.pop()
        return len(self.queue)
