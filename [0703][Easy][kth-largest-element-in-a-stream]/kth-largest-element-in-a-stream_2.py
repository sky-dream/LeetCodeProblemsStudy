# 小顶堆
import heapq
class KthLargest:
    def __init__(self, k, nums):
        self.pool = nums
        heapq.heapify(self.pool)
        self.k = k
        while len(self.pool) > k:
            heapq.heappop(self.pool)

    def add(self, val) :
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)
        return self.pool[0]
    
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