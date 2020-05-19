# -*- coding: utf-8 -*-  
# leetcode time     cost : 56 ms
# leetcode memory   cost : 13.8 MB
# solution 1, hash map,
# solution 1, hash map,
class Solution:
    def romanToInt(self, s: str) -> int:
        Roman2Int = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        Int = 0
        n = len(s)

        for index in range(n - 1):
            # if small num char is before big char, then use it as a negative value
            if Roman2Int[s[index]] < Roman2Int[s[index + 1]]:
                Int -= Roman2Int[s[index]] 
            else:
                Int += Roman2Int[s[index]]

        return Int + Roman2Int[s[-1]]


def main():
    inputX,expectRes = "MCMXCIV",1994
    obj = Solution()
    result = obj.romanToInt(inputX)
    try:
        assert result == expectRes
        print("passed, result is follow expect:",result)
    except AssertionError as aError:
        print('failed, result >> ', result,"<< is wrong, ","expect is : "+ expectRes)
    
if __name__ =='__main__':
    main() 