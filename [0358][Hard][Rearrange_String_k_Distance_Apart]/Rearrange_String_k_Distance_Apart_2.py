# solution 2, solution 3, analysis and design..
# leetcode time     cost : 116 ms
# leetcode memory   cost : 13.8 MB 
# Time  Complexity: O(M)
# Space Complexity: O(1)
from collections import Counter
import collections
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k <= 1: return s
        c = Counter(s)
        n = len(s)
        #set count value as negative value to match the min heap usage, the min top is the max counter.
        charPair = []
        for key, v in c.items():
            charPair = charPair + [[key,v]]            
        charDictList = sorted(charPair,key=lambda x:x[1],reverse=False)
        result = ""
        maxIndex = len(charDictList)-1
        while charDictList[maxIndex][1]:
            i = 0;
            validCharInSubLoop =0;
            while (i < k):
                if (charDictList[maxIndex][1] == 0):
                    break;
                if (i <= maxIndex and charDictList[maxIndex-i][1] > 0):
                    result = result + charDictList[maxIndex-i][0]
                    charDictList[maxIndex-i][1] = charDictList[maxIndex-i][1] -1
                    #used to counter the valid char count in this sub group
                    validCharInSubLoop= validCharInSubLoop +1
                i = i + 1
                # for sub loop not include last loop, if sub loop finished with no enough valid char can be use.
                if (charDictList[maxIndex][1] > 0 and i == k and validCharInSubLoop != k): 
                    return ""
            charDictList = sorted(charDictList,key=lambda x:x[1],reverse=False)
        return result 
    
def main():
    str1 = "aabbccdddfffff"         #expect is "fdafbcfdafbcdf"
    str2 = "aabbccdddffffff";         #expect is ""
    k = 3
    s = Solution()
    res = s.rearrangeString(str1,k) 
    print("in python,rearrangeString res is : "+res)
    res = s.rearrangeString(str2,k) 
    print("in python,rearrangeString res is : "+res)
if __name__ =='__main__':
    main()    