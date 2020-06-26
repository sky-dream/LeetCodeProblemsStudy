# leetcode time     cost : 80 ms
# leetcode memory   cost : 13.7 MB
# Time  Complexity: O(N)
# Space Complexity: O(N)
# solution 1, convert int to string
class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversed_str = str_x = str(x)
        reversed_str = str_x[::-1]
        return reversed_str == str_x
    
    def isPalindrome_2(self, x: int) -> bool:
        str_x = str(x)
        n = len(str_x)
        l,r = 0,n-1
        while l<r:
            if str_x[l]!=str_x[r]:
                return False
            l+=1
            r-=1
        return True
    
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