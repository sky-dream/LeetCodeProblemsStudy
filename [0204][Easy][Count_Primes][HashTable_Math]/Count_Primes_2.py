# leetcode time     cost : 676 ms, 
# leetcode memory   cost : 27.3 MB 
# solution 2, Sieve of Eratosthenes
# https://leetcode-cn.com/problems/count-primes/solution/ru-he-gao-xiao-pan-ding-shai-xuan-su-shu-by-labula/
class Solution:
    def countPrimes(self, n: int) -> int:
        isPrime = [True for _ in range(n+1)]
        
        # only update those none prime nums until sqrt(n) to save time
        i = 2
        while (i*i < n):
            if (isPrime[i]): 
                # check current num 'i' is prime or not
                # if num_x = i*i +i (i in [2,sqrt(n)]), then num_x is not prime
                j = i * i
                while (j < n):
                    isPrime[j] = False 
                    j+=i      
            i +=1
        # count all the prime nums
        count = 0
        for i in range(2,n):
            if (isPrime[i]):
                count+=1
        return count

def main():
    n = 10  # expect is 4,
    obj = Solution()
    result = obj.countPrimes(n)       
    print("return result is ",result)
    
if __name__ =='__main__':
    main() 