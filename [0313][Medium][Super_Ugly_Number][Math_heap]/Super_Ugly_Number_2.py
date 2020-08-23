# Time  Complexity: O(N*k)
# Space Complexity: O(N+k)
# solution 2, heap
from typing import List
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        import heapq
        heap = [1]
        n -= 1
        while n:
            tmp = heapq.heappop(heap)
            while heap and tmp == heap[0]:
                tmp = heapq.heappop(heap)
            for p in primes:
                t = p * tmp
                heapq.heappush(heap, t)
            n -= 1
        return heapq.heappop(heap)

def main():  
    n = 12
    primes = [2,7,13,19]   
    obj = Solution()
    result = obj.nthSuperUglyNumber(n, primes)
    print("return result is: ",result)
    
if __name__ =='__main__':
    main() 