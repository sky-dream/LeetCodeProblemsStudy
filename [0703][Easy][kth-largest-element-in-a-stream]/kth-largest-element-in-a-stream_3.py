import heapq

class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.heap = []
        for n in nums:
            self.add(n)
        
    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.heap) < self.k:          
            heapq.heappush(self.heap, val)
        elif self.heap[0] < val:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)
        return self.heap[0]
    
def main():
    k = 3
    nums = [4,5,8,2]
    obj = KthLargest(k, nums)
    param_1 = obj.add(3)
    param_1 = obj.add(5)
    param_1 = obj.add(10)
    param_1 = obj.add(9)
    print("last return value is "+str(param_1));
    
if __name__ =='__main__':
    main()  
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)