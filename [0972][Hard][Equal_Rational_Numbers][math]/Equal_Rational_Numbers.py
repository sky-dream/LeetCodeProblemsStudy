# leetcode time     cost : 40 ms
# leetcode memory   cost : 13.8 MB 
# Time  Complexity: O(1)
# Space  Complexity: O(1)
# math
from fractions import Fraction
# Fraction(numerator=0, denominator=1),
# 第一个参数是分子，默认为0；第二个参数为分母，默认为1。比如Fraction(2)=2；
class Solution(object):
    def isRationalEqual(self, S, T):
        def convert(S):
            if '.' not in S:
                return Fraction(int(S), 1)
            # list.index(x[, start[, end]]),返回查找对象的索引位置，如果没有找到对象则抛出异常
            i = S.index('.')
            # 获取整数部分的值
            ans = Fraction(int(S[:i]), 1)
            # 处理剩余小数部分
            S = S[i+1:]
            if '(' not in S:
                if S:
                    # 0.1234, value = 1234/(10**4)
                    ans += Fraction(int(S), 10 ** len(S))
                return ans

            i = S.index('(')
            # 0.5(123), 5/10 + 123*( 1/1000 + (1/1000)**2 + (1/1000)**3 + ...)/10
            if i:
                ans += Fraction(int(S[:i]), 10 ** i)
            # get the repeat part in the round bracket
            S = S[i+1:-1]
            j = len(S)
            # 等比数列求和，n>1时,s(n) = a1*(1-q**n)/(1-q)
            ans += Fraction(int(S), 10**i * (10**j - 1))
            return ans

        return convert(S) == convert(T)

def main():
    S, T = "0.(52)","0.5(25)"
    expect = True
    obj = Solution()
    result = obj.isRationalEqual(S, T)
    try:
        assert result == expect
        print("passed, result is follow expect:",result)
    except AssertionError as aError:
        print('failed, result is wrong', result, aError.__str__())
    
if __name__ =='__main__':
    main()   