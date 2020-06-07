# leetcode time     cost : 156 ms
# leetcode memory   cost : 13.7 MB
# Time  Complexity: O(m*n)
# Space Complexity: O(m+n)
# solution 1, simulate the mannual multiply bit by bit
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        results = []
        for  i  in  range(len(num1)+len(num2)):
            results.append(0)
        for  i  in  range(len(num1)-1,-1,-1):
            for  j  in  range(len(num2)-1,-1,-1):
            #这里有个细节，对于字符串需要先计算最小的一位，从个位开始从左往右计算
            #数位有利于进位加到前面的数值中去
                p1,p2 = i+j,i+j+1
                mul = ((ord(num1[i]))-((ord('0'))))*((ord(num2[j]))-((ord('0'))))
                sums = mul+results[p2]        # 需要考虑results[p2]由于前一步计算进位得到的值
                results[p2] = sums%10
                results[p1] = results[p1]+sums//10    # 将进位数值累加到更高的位
                #注意这里有个细节，必须先计算i+j+1后面一位的数值，再计算前面一位
                #i+j的数值，这样方便于把后面的数值带来的进位加到前面数值的上面
        cur = 0
        while   cur < len(results) and results[cur] == 0:
            cur = cur+1
        #去除前导0
        resultstring = ''
        for  i  in  range(cur,len(results)):
            resultstring = resultstring+(str)(results[i])
        if  resultstring == '':
            return  '0'
        return   resultstring
    
def main():
    num1, num2,expectRes = "123","456" ,"56088"
    obj = Solution()
    result = obj.multiply(num1, num2)
    try:
        assert result == expectRes
        print("passed, result is follow expect:",result)
    except AssertionError as aError:
        print('failed, result >> ', result,"<< is wrong, ","expect is : "+ expectRes)
    
if __name__ =='__main__':
    main()  