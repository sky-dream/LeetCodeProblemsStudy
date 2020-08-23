# Time  Complexity: O(result num value)
# Space Complexity: O(1)
# solution 4, brute force, backtracking, max time exceeded.
from typing import List
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        count = 1
        num = 1
        def isValid(num,primes):
            res = False
            if num==1:
                return True
            for x in primes:
                left = num//x
                if left*x!=num:
                    continue
                else:
                    res = res or isValid(left,primes)
            return res
        while (count <=n ):
            if isValid(num,primes):
                count+=1
            num+=1
        return num-1

def main():  
    n = 12
    primes = [2,7,13,19]   
    obj = Solution()
    result = obj.nthSuperUglyNumber(n, primes)
    print("return result is: ",result)
    
if __name__ =='__main__':
    main() 