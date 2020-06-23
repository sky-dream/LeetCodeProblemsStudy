# leetcode time     cost : 212 ms
# leetcode memory   cost : 24.8 MB 
# solution 3, 2 priority queue,
# Time  Complexity: O(logN)
# Space Complexity: O(N)
import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if len(self.max_heap) == len(self.min_heap):
            heapq.heappush(self.min_heap, -heapq.heappushpop(self.max_heap, -num))
        else:
            heapq.heappush(self.max_heap, -heapq.heappushpop(self.min_heap, num))

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (self.min_heap[0] - self.max_heap[0]) / 2
        else:
            return self.min_heap[0]

# Your MedianFinder object will be instantiated and called as such:


def main():
    obj = MedianFinder()
    obj.addNum(1)
    obj.addNum(2)
    obj.addNum(3)
    param_2 = obj.findMedian()
    print("in python,res is : ",param_2)
if __name__ =='__main__':
    main() 