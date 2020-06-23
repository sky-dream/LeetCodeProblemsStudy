# leetcode time     cost : 244 ms
# leetcode memory   cost : 24.5 MB 
# solution 2, insert sorting
# Time  Complexity: O(NlogN)
# Space Complexity: O(1)
import bisect
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """

        self.data = []

    def addNum(self, num: int) -> None:
        bisect.insort_left(self.data, num)

    def findMedian(self) -> float:
        n = len(self.data)
        mid = (n - 1) // 2
        if n % 2 == 1:
            return self.data[mid]
        else:
            return (self.data[mid] + self.data[mid + 1]) / 2


def main():
    obj = MedianFinder()
    obj.addNum(1)
    obj.addNum(2)
    obj.addNum(3)
    param_2 = obj.findMedian()
    print("in python,res is : ",param_2)
if __name__ =='__main__':
    main() 