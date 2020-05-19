# -*- coding: utf-8 -*-  
# leetcode time     cost : 64 ms
# leetcode memory   cost : 13.6 MB
# solution 1, hash map,
class Solution:
    def romanToInt(self, s: str):
        dict1 = {
            "I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000, 
            "IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900
        }
        sum = 0
        i = 0
        while(i < len(s)):
            if s[i:i+2] in dict1.keys():
                sum+=dict1[s[i:i+2]]
                i+=2
            elif s[i] in dict1.keys():
                sum+=dict1[s[i]]
                i+=1
        return sum

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