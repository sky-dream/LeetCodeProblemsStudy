# Time  Complexity: O(N*k)
# Space Complexity: O(N+k)
# solution 3, based on DP and heap
# https://leetcode-cn.com/problems/super-ugly-number/solution/dong-tai-gui-hua-dui-by-powcai/
from typing import List
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        import heapq
        uglies = [0] * n
        uglies[0] = 1
        visited = set()
        visited.add(1)
        primes_to_uglies_idx = [0] * len(primes)
        heap = []
        for idx, prime in enumerate(primes):
            heapq.heappush(heap, [prime, idx])
            visited.add(prime)

        for i in range(1, n):
            uglies[i], k = heapq.heappop(heap)

            while primes[k] * uglies[primes_to_uglies_idx[k]] in visited:
                primes_to_uglies_idx[k] += 1
            heapq.heappush(heap, [primes[k] * uglies[primes_to_uglies_idx[k]], k])
            visited.add(primes[k] * uglies[primes_to_uglies_idx[k]])
        return uglies[-1]

def main():  
    n = 12
    primes = [2,7,13,19]   
    obj = Solution()
    result = obj.nthSuperUglyNumber(n, primes)
    print("return result is: ",result)
    
if __name__ =='__main__':
    main() 