# Time  Complexity: O(N*k)
# Space Complexity: O(N+k)
# solution 1, DP
# https://leetcode-cn.com/problems/super-ugly-number/solution/dong-tai-gui-hua-dui-by-powcai/
from typing import List
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        uglies = [0] * n
        primes_to_uglies_idx = [0] * len(primes)
        uglies[0] = 1
        for i in range(1, n):
            # similar to a heap with k elements
            uglies[i] = min(x * uglies[y] for x, y in zip(primes, primes_to_uglies_idx))  
            # update the array primes_to_uglies_idx 
            for j in range(len(primes)):
                if uglies[i] >= primes[j] * uglies[primes_to_uglies_idx[j]]:
                    primes_to_uglies_idx[j] += 1
        return uglies[-1]

def main():  
    n = 12
    primes = [2,7,13,19]   
    obj = Solution()
    result = obj.nthSuperUglyNumber(n, primes)
    print("return result is: ",result)
    
if __name__ =='__main__':
    main() 