# -*- coding: utf-8 -*-  
# leetcode time     cost : 36 ms
# leetcode memory   cost : 13.7 MB
# solution 3, string to int
class Solution:
    def grayCode(self, n: int) -> [int]:
        num = "0" * n
        res = [0]
        c = 2 ** n
        while len(res) < c:
            if num[-1] == "0":
                num = num[:-1] + "1"
                res.append(int(num, 2))
            else:
                num = num[:-1] + "0"
                res.append(int(num, 2))
            # print(num)

            if len(res) == c:
                break
            idx = num.rfind("1")
            if num[idx - 1] == "0":
                num = num[:idx - 1] + "1" + num[idx:]
            else:
                num = num[:idx - 1] + "0" + num[idx:]
            # print(num)
            res.append(int(num, 2))

        return res
    
def main():
    code = 2             #expect is [0,1,3,2]
    obj = Solution()
    result = obj.grayCode(code)
    print("return result is :",result)
    
if __name__ =='__main__':
    main()   