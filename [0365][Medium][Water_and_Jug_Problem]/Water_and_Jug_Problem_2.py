# leetcode time     cost : 40 ms
# leetcode memory   cost : 13.4 MB 
# Time  Complexity: O(log(min(x,y)))
# Space Complexity: O(1)
# solution 2, 贝祖定理，ax+by=z，当且仅当 z 是 x,y 的最大公约数的倍数 有解
import math
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if x + y < z:
            return False
        if x == 0 or y == 0:
            return z == 0 or x + y == z
        # math.gcd(x, y)求x,y 的最大公约数，辗转相除定理
        return z % math.gcd(x, y) == 0
    
    def gcd(self,a, b):
        return  a if b == 0 else gcd(b, a % b)
    
def main():
    x , y , z = 3, 4, 5     #expect is true   
    obj = Solution()
    res = obj.canMeasureWater(x , y , z)
    print("return value is ",res);
    
if __name__ =='__main__':
    main() 
