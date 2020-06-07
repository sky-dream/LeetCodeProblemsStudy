# leetcode time     cost : 60 ms
# leetcode memory   cost : 13.6 MB 
# Time  Complexity: O(m+n)
# Space Complexity: O(m+n)
# refer to No.43
# solution 2, 2pointers, simulate the mannual adding bit by bit
class Solution:
    def addStrings(self, num1: str, num2: str):
        res = ""
        i, j, carry = len(num1) - 1, len(num2) - 1, 0
        # start from right side.
        while i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            tmp = n1 + n2 + carry
            carry = tmp // 10
            # add the new res string as the new prefix in the left
            res = str(tmp % 10) + res   
            # decrease the 2 index pointers 
            i, j = i - 1, j - 1
        return "1" + res if carry else res   
    
def main():
    num1, num2,expectRes = "123","456" ,"579"
    obj = Solution()
    result = obj.addStrings(num1, num2)
    try:
        assert result == expectRes
        print("passed, result is follow expect:",result)
    except AssertionError as aError:
        print('failed, result >> ', result,"<< is wrong, ","expect is : "+ expectRes)
    
if __name__ =='__main__':
    main()  