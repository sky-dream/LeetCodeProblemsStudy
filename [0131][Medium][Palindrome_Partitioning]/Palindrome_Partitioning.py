# -*- coding: utf-8 -*-  
# leetcode time     cost : 40 ms
# leetcode memory   cost : 13.9 MB
# Time  Complexity: O(N*N)
# Space Complexity: O(N*N)
# solution 1, DP
class Solution:
    def partition(self, s: str) -> [[str]]:
    #def partition(self, s: str) -> List[List[str]]:
        strListCollection = [[s[0]]]
        for i in range(1,len(s)):
            for strList in strListCollection:
                if len(strList)>1 and s[i] == strList[-2]:
                    strListCollection.append(strList[:-2]+[strList[-2]+strList[-1]+s[i]])
                if s[i] == strList[-1]:
                    strListCollection.append(strList[:-1]+[s[i]*2])
                strList.append(s[i])
        return strListCollection

def main():
    code = "aab"             #expect is [["a","a","b"],["aa","b"]]
    obj = Solution()
    result = obj.partition(code)
    print("return result is :",result)
    
if __name__ =='__main__':
    main() 