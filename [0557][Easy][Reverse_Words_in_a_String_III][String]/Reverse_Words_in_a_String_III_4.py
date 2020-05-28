# solution 3, reverse whole string, then reverse the word,
# Time  Complexity: O(N)
# Space Complexity: O(1)
# “neeuq gard evol I”-----> s[::-1]
# ['neeuq', 'gard', 'evol', 'I']-----> s[::-1].split(" ")
# ['I', 'evol', 'gard', 'neeuq']-----> s[::-1].split(" ")[::-1]
# “I evol gard neeuq”-----> join the str
class Solution(object):
    def reverseWords(self, s):
         return " ".join(s[::-1].split(" ")[::-1])
    
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