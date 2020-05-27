# -*- coding: utf-8 -*-  
# solution 1, split, cast to int from str,loop twice,
# Time  Complexity: O(N+M+max(N,M))
# Space Complexity: O(N+M)
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        nums1 = version1.split('.')
        nums2 = version2.split('.')
        n1, n2 = len(nums1), len(nums2)
        
        # compare versions
        for i in range(max(n1, n2)):
            i1 = int(nums1[i]) if i < n1 else 0
            i2 = int(nums2[i]) if i < n2 else 0
            if i1 != i2:
                return 1 if i1 > i2 else -1
        
        # the versions are equal
        return 0 

def main():
    inputX1,inputX2,expectRes = "0.1","0.3",-1
    obj = Solution()
    result = obj.compareVersion(inputX1,inputX2)
    try:
        assert result == expectRes
        print("passed, result is follow expect:",result)
    except AssertionError as aError:
        print('failed, result >> ', result,"<< is wrong, ","expect is : "+ expectRes)
    
if __name__ =='__main__':
    main()