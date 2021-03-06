class KthLargest:
    def __init__(self, k, nums):
        self.nums = nums
        self.k = k
        self.nums.sort(reverse = True)
        while len(self.nums) > k:
            self.nums.pop()

    def add(self, val):
        self.nums.append(val)
        self.nums.sort(reverse = True)
        if len(self.nums) > self.k:
            self.nums.pop()
        return self.nums[-1]
    
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