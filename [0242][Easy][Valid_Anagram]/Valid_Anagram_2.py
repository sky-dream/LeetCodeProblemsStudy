class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        se = set(s)
        if se == set(t):
            for i in se:
                # 直接比较 每个字符元素char 在2个string的个数
                if s.count(i) != t.count(i):return False
            return True
        else:
            return False
    
    
def main():
    str1 = "anagramsq";
    str2 = "nagaramqs";
    Solution_obj = Solution()
    result = Solution_obj.isAnagram(str1, str2);
    print("In c code,result value is "+("FALSE" if result is False else "TRUE"));
    
if __name__ =='__main__':
    main()  