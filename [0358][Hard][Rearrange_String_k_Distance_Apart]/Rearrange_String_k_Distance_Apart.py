# solution 2, greedy min heap.
# leetcode time     cost : 116 ms
# leetcode memory   cost : 13.7 MB 
# Time  Complexity: O(NlogA))，其中 NN 为 SS 的长度，AA 为字母表的大小。如果 AA 是一个定值，那么复杂度为 O(N)O(N)。
# Space Complexity: O(A)。如果 AA 是一个定值，那么复杂度为 O(1)O(1)。
from collections import Counter
import heapq
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k <= 1: return s
        c = Counter(s)
        n = len(s)
        #set count value as negative value to match the min heap usage, the min top is the max counter.
        heap = [(-v, k) for k, v in c.items()]
        heapq.heapify(heap)
        res = ""
        while heap:
            tmp = []
            for _ in range(k):
                if not heap:
                    return res if len(res) == n else ""
                num, alp = heapq.heappop(heap)
                num += 1
                res += alp
                if num != 0:
                    tmp.append((num, alp))
            # push back not used char into the min heap for the next loop k usage.
            for t in tmp:
                heapq.heappush(heap, t)
        return res 

#python heapq(堆， 即优先队列PriorityQueue)常用函数             描 述
#heappush(heap, x)                                              将x压入堆中
#heappop(heap)                                                  从堆中弹出最小的元素
#heapify(heap)                                                  让列表具备堆特征
#heapreplace(heap, x)                                           弹出最小的元素，并将x压入堆中
#nlargest(n, iter)                                              返回iter中n个最大的元素
#nsmallest(n, iter)                                             返回iter中n个最小的元素