# solution 2, slice twice, no need loop
# Time  Complexity: O(N)
# Space Complexity: O(1)
class Solution(object):
    def reverseWords(self, s):
        return " ".join(s.split(" ")[::-1])[::-1]
    
def main():
    inputX1,expectRes = "Let's take LeetCode contest werwwer","s'teL ekat edoCteeL tsetnoc rewwrew"
    obj = Solution()
    result = obj.reverseWords(inputX1)
    try:
        assert result == expectRes
        print("passed, result is follow expect:",result)
    except AssertionError as aError:
        print('failed, result >> ', result,"<< is wrong, ","expect is : "+ expectRes)
    
if __name__ =='__main__':
    main()