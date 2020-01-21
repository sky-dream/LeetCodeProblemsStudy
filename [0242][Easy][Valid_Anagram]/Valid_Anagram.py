class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        else:
            #结果字典
            dic = {}
            #先遍历s，数每个字符出现的次数，存在字典dic中，key是字符，value是出现次数
            for i in s:
                if i in dic:
                    dic[i] +=1
                else:
                    dic[i] = 1
            #遍历t，遇见相同字符，就在dic中减一；遇见不同字符，直接返回false
            for i in t:
                if i in dic:
                    dic[i] -= 1
                else:
                    return False
            #遍历结果字典，是否每个value都为0
            for i in dic:
                if dic[i] != 0:
                    return False
        return True
    
    
def main():
    str1 = "anagram";
    str2 = "nagaram";
    Solution_obj = Solution()
    result = Solution_obj.isAnagram(str1, str2);
    print("In c code,result value is "+("FALSE" if result is False else "TRUE"));
    
if __name__ =='__main__':
    main()  