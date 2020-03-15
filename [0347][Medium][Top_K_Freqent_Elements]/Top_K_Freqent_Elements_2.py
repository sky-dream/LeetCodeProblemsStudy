# leetcode time     cost : 120 ms
# leetcode memory   cost : 17.9 MB 
# Time  Complexity: O(N*logK)
# Space Complexity: O(N)
# similar as 215,358, heap, sort
import collections
import heapq
class Solution:
    def topKFrequent(self, nums, k):
        count = collections.Counter(nums)   
        return heapq.nlargest(k, count.keys(), key=count.get) 

def main():
    array,k = [1,1,1,2,2,3],2      #expect is [1,2]   
    obj = Solution()
    res = obj.topKFrequent(array,k)
    print("return value is ",res);
    
if __name__ =='__main__':
    main() 
    

#python heapq(堆， 即优先队列PriorityQueue)常用函数             描 述
#heappush(heap, x)                                              将x压入堆中
#heappop(heap)                                                  从堆中弹出最小的元素
#heapify(heap)                                                  让列表具备堆特征
#heapreplace(heap, x)                                           弹出最小的元素，并将x压入堆中
#nlargest(n, iter)                                              返回iter中n个最大的元素
#nsmallest(n, iter)                                             返回iter中n个最小的元素