# leetcode time     cost : 100 ms
# leetcode memory   cost : 13.8 MB
# Time  Complexity: O(N)
# Space Complexity: O(1)
# solution 2, convert int value into num list
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        nums = []
        while x>0:
            num = x%10
            nums.append(num)
            x = x//10
        l,r = 0,len(nums)-1
        while l<r:
            if nums[l]!=nums[r]:
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