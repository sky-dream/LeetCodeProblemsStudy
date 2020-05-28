# solution 1, straightforward
# Time  Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def reverseStr(self,slist,l,r):
        while l<r:
            slist[l],slist[r] = slist[r],slist[l]
            l,r = l+1,r-1
        return slist    
    def reverseWords(self, s: str) -> str:
        slist = list(s)
        l = 0
        for i in range(len(slist)):
            if slist[i]==' ':
                slist = self.reverseStr(slist,l,i-1)
                l = i+1
            if i == len(slist)-1:
                slist = self.reverseStr(slist,l,i)
        res = ''
        return res.join(slist)
    
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