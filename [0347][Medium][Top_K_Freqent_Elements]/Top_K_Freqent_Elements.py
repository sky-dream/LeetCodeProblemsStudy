# leetcode time     cost : 168 ms
# leetcode memory   cost : 14 MB 
# Time  Complexity: O(N*logK)
# Space Complexity: O(N)
# similar as 215,358, heap, sort
import collections
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = collections.Counter(nums)
        n = len(nums)
        # use a min heap, max freq is -x, on the top,v is the freq,
        for num, freq in freqDict.items():
            heap = [(-freq, num) for num, freq in freqDict.items()]
        heapq.heapify(heap)
        res = []
        # loop to get the k th freq from the heap
        while heap:
            for i in range(k):
                freq, num = heapq.heappop(heap)
                res.append(num)
            break

            # how to handle when there are (k+1) elements with max freq 
            if heap:
                freqTemp, numTemp = heapq.heappop(heap)
                # check whether still elements has the same k th freq
                if freqTemp == freq:
                    res.append(numTemp)
                else:
                    break
            else:
                break
        return res 

def main():
    array,k = [1,1,1,2,2,3],2      #expect is [1,2]   
    obj = Solution()
    res = obj.findKthLargest(array,k)
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