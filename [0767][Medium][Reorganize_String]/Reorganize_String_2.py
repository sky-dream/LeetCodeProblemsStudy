# solution 2, based on the greedy heap.
# leetcode time     cost : 16 ms
# leetcode memory   cost : 11.8 MB 
# Time  Complexity: O(NlogA))，其中 NN 为 SS 的长度，AA 为字母表的大小。如果 AA 是一个定值，那么复杂度为 O(N)O(N)。
# Space Complexity: O(A)。如果 AA 是一个定值，那么复杂度为 O(1)O(1)。
import heapq 
class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        pq = [(-S.count(x), x) for x in set(S)]
        heapq.heapify(pq)
        if any(-nc > (len(S) + 1) / 2 for nc, x in pq):
            return ""

        ans = []
        while len(pq) >= 2:
            nct1, ch1 = heapq.heappop(pq)
            nct2, ch2 = heapq.heappop(pq)
            #This code turns out to be superfluous, but explains what is happening
            #if not ans or ch1 != ans[-1]:
            #    ans.extend([ch1, ch2])
            #else:
            #    ans.extend([ch2, ch1])
            ans.extend([ch1, ch2])
            if nct1 + 1: heapq.heappush(pq, (nct1 + 1, ch1))
            if nct2 + 1: heapq.heappush(pq, (nct2 + 1, ch2))

        return "".join(ans) + (pq[0][1] if pq else '')
    
def main():
    string1 = "aabcc" #expect is "abcac", or "acabc"
    obj = Solution()
    result = obj.reorganizeString(string1)
    print("return result is "+result);

if __name__ =='__main__':
    main() 
#python heapq(堆， 即优先队列PriorityQueue)常用函数             描 述
#heappush(heap, x)                                              将x压入堆中
#heappop(heap)                                                  从堆中弹出最小的元素
#heapify(heap)                                                  让列表具备堆特征
#heapreplace(heap, x)                                           弹出最小的元素，并将x压入堆中
#nlargest(n, iter)                                              返回iter中n个最大的元素
#nsmallest(n, iter)                                             返回iter中n个最小的元素