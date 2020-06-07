# leetcode time     cost : 72 ms
# leetcode memory   cost : 13.8 MB 
# Time  Complexity: O(m+n)
# Space Complexity: O(m+n)
# refer to No.43
# solution 1, simulate the mannual adding bit by bit
class Solution:
    def addStrings(self, num1: str, num2: str):
        results = []
        n = max(len(num1), len(num2))
        l1,l2 = len(num1), len(num2)
        # result多增加一位，防止最高位有进位
        for  i  in  range(n+1):
            results.append(0)
        for  i  in  range(n):
            #这里有个细节，对于字符串需要先计算最小的一位，从个位开始从左往右计算
            #数位有利于进位加到前面的数值中去
            val_1 = (ord(num1[l1-1-i]))-((ord('0'))) if i<(l1) else 0
            val_2 = (ord(num2[l2-1-i]))-((ord('0'))) if i<(l2) else 0
            sum_value = val_1 + val_2
            sums = sum_value + results[n-i]        # 需要考虑results[p2]由于前一步计算进位得到的值
            results[n-i] = sums%10
            results[n-i-1] = results[n-i-1]+sums//10    # 将进位数值累加到更高的位
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