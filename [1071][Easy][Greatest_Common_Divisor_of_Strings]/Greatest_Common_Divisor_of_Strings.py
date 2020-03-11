# leetcode time     cost : 36 ms
# leetcode memory   cost : 13.6 MB 
# solution 2, enumeration optimized
import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        candidate_len = math.gcd(len(str1), len(str2))
        candidate = str1[: candidate_len]
        if candidate * (len(str1) // candidate_len) == str1 and candidate * (len(str2) // candidate_len) == str2:
            return candidate
        return ''
    
def main():
    str_a = "ABCABC"
    str_b = "ABC"
    obj = Solution()
    result = obj.gcdOfStrings(str_a,str_b)
    print("return value is ",result);
    
if __name__ =='__main__':
    main()  