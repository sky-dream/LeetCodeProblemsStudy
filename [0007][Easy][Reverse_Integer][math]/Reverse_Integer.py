# leetcode time     cost : 40 ms
# leetcode memory   cost : 13.7 MB
# Time  Complexity: O(logX)
# Space Complexity: O(1)
class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        flag = 1 if x>0 else -1
        while x != 0:
            num = abs(x)%10
            res = res*10 + num
            x = abs(x)//10  
        return res*flag if - 2**31 < res <(2**31 -1 ) else 0
def main():
    inputX,expectRes = -3210, -123
    obj = Solution()
    
    result = obj.reverse(inputX)
    try:
        assert result == expectRes
        print("passed, result is follow expect:",result)
    except AssertionError as aError:
        print('failed, result >> ', result,"<< is wrong, ","expect is : ",expectRes)
    
if __name__ =='__main__':
    main() 