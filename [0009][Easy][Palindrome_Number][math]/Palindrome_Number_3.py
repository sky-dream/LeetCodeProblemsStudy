# leetcode time     cost : 88 ms
# leetcode memory   cost : 13.7 MB
# Time  Complexity: O(N)
# Space Complexity: O(1)
# solution 2, convert half part int value into reversed num
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0 or (x % 10 == 0 and x != 0)):
            return False
        reversedNumber = 0
        # loop half digits of x
        while (x > reversedNumber) :
            reversedNumber = reversedNumber * 10 + x % 10
            x //= 10
        # the digits of x maybe even or odd
        return x == reversedNumber or x == reversedNumber // 10
    
def main():
    inputX,expectRes = -3210, False
    obj = Solution()
    
    result = obj.isPalindrome(inputX)
    try:
        assert result == expectRes
        print("passed, result is follow expect:",result)
    except AssertionError as aError:
        print('failed, result >> ', result,"<< is wrong, ","expect is : ",expectRes)
    
if __name__ =='__main__':
    main() 