# leetcode time     cost : 24 ms
# leetcode memory   cost : 13.8 MB 
# Time  Complexity: O(1)
# Space Complexity: O(1)
# solutioin 2, add time stamp to queue, count the length of the queue
class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timequeue=[]
        
    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.timequeue.append(timestamp)
        # if self.timequeue[0]<timestamp-300+1:
        #     self.timequeue.pop()

    def getHits(self, timestamp: int) -> int:
        n=0
        m=0
        for i in range(len(self.timequeue)):
            if self.timequeue[i]>=timestamp-300+1:
                n=i
                m+=1
                break
        if m:
            return len(self.timequeue)-n
        else:
            return 0

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)