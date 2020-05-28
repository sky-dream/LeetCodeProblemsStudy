# solution 1, split and loop the list, then join the string
# Time  Complexity: O(N)
# Space Complexity: O(1)
# solution 1,
class Solution(object):
    def reverseWords(self, s):
        return " ".join(word[::-1] for word in s.split(" "))
    
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