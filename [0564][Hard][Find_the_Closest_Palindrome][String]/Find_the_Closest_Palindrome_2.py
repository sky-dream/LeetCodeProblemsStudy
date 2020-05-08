# -*- coding: utf-8 -*-  
# leetcode time     cost : 32 ms
# leetcode memory   cost : 13.7 MB
'''
先取前一半（N）镜像成回文串，跟原数做比较
如果等于原数，就取两个数，一个大于原数的回文，一个小于原数的回文。
如果大于原数，就将前一半 N-1 加上剩余的一半再做一次镜像，得到一个小于原数的回文。
如果小于原数，就将前一半 N+1 加上剩余的一半再做一次镜像，得到一个大于原数的回文。

其中要考虑N-1的时候的特殊情况，如 1-1，10-1，100-1，等
这些特殊情况下的处理方式都是一样的，返回原数长度 l-1 个 9即可。
'''
class Solution:
    def mirror(self,n:str):
        length = len(n)
        half = length // 2
        if length % 2 == 0:
            return n[:half] + ''.join(reversed(n[:half]))
        else:
            return n[:half+1] + ''.join(reversed(n[:half]))

    def get_small(self,n:str):
        half = len(n) // 2
        if len(n) % 2 == 0:
            half -= 1
        half_num = int (n[:half+1])
        half_str = str (half_num-1)
        if half_str == '0' or len(half_str) < half + 1:
            return '9'*(len(n)-1)
        else:
            return self.mirror(half_str+n[half+1:])
    
    def get_big(self, n:str):
        half = len(n) // 2
        if len(n) % 2 == 0:
            half -= 1
        half_num = int (n[:half+1])
        half_str = str (half_num+1)

        return self.mirror(half_str+n[half+1:])


    def nearestPalindromic(self, n: str) -> str:
        num = int(n)
        if n == 0:
            return "1"
        if num < 10:
            return str(num - 1)
        
        palindromic_str = self.mirror(n)

        palindromic_num = int(palindromic_str)
        if palindromic_num > num:
            small_num = int(self.get_small(n))
            big_num = palindromic_num
        elif palindromic_num < num:
            small_num = palindromic_num
            big_num = int(self.get_big(n))
        else:
            small_num = int(self.get_small(n))
            big_num = int(self.get_big(n))

        if abs(big_num - num) < abs(small_num - num):
            return str(big_num)
        else:
            return str(small_num)


def main():
    inputX,expectRes = "1234","1221"
    obj = Solution()
    result = obj.nearestPalindromic(inputX)
    try:
        assert result == expectRes
        print("passed, result is follow expect:",result)
    except AssertionError as aError:
        print('failed, result >> ', result,"<< is wrong, ","expect is : "+ expectRes)
    
if __name__ =='__main__':
    main() 