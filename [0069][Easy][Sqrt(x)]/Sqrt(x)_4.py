# solution 4, Integer Newton,
# leetcode time     cost : 36 ms
# leetcode memory   cost : 13.1 MB 
# Time  Complexity: O(logN)
# Space Complexity: O(1)
class Solution:
    def mySqrt(self, x):
        if x < 2:
            return x
        
        x0 = x
        x1 = (x0 + x / x0) / 2
        while abs(x0 - x1) >= 1:
            x0 = x1
            x1 = (x0 + x / x0) / 2           
        return int(x1)
# y = f(x[k+1]) + f'(x[k])*(x[k+1]-x[k]) = 0, if f'(x[k])!=0, then x[k+1] = x[k] - f(x[k])/f'(x[k]),
# f(x[k]) = x^2 - a = 0, f'(x[k]) = 2x, then x[k+1] = x[k] -(x[k]^2 - a)/2(x[k]) = (x[k] + a/x[k])/2,
def main():
    num = 20000;
    Solution_obj = Solution()
    result = Solution_obj.mySqrt(num);
    print("result value is "+str(result));
    
if __name__ =='__main__':
    main()  