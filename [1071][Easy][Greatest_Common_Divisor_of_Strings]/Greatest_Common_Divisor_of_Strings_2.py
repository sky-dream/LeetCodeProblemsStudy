# leetcode time     cost : 40 ms
# leetcode memory   cost : 13.5 MB 
# solution 3, dfs
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        str1Length, str2Length = len(str1), len(str2)
        
        if str2Length > str1Length: # Ensures the longer string is str1 and shorter or equal string is str2
            return self.gcdOfStrings(str2, str1)
        
        if str1[:str2Length] == str2: # Check if shorter string (str2) is a prefix in longer string (str1)
		
            if str1Length == str2Length: # If str1 and str2 are of the same length then we have found the common divisor
                return str2
            
            return self.gcdOfStrings(str2, str1[str2Length:]) # return the gcd of the str2 and str1 minus the prefix

        return ""
    
def main():
    str_a = "ABCABC"
    str_b = "ABC"
    obj = Solution()
    result = obj.gcdOfStrings(str_a,str_b)
    print("return value is ",result);
    
if __name__ =='__main__':
    main()  