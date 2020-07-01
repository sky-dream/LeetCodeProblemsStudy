# leetcode time     cost : -- ms, max time exceeded
# leetcode memory   cost : -- MB 
# Time  Complexity: O(N**1.5)
# Space Complexity: O(1)
# solution 1
class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0
        for i in range(2,n):
            if (self.isPrime(i)):
                count+=1
        return count;
    # 判断整数 n 是否是素数
    def isPrime(self,n):
        i = 2
        while (i*i <= n):
            if (n % i == 0):
                # 有其他整除因子
                return False
            i +=1    
        return True

def main():
    n = 10  # expect is 4,
    obj = Solution()
    result = obj.countPrimes(n)       
    print("return result is ",result)
    
if __name__ =='__main__':
    main() 