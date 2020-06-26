# -*- coding: utf-8 -*-  
# Time  Complexity: O(N)
# Space Complexity: O(N)
# solution 2, dict and stack
class Solution:
    def simplifyPath(self, path: str) -> str:
        r = []
        for s in path.split('/'):
            # if s!= '',or '.',or '..',key is not in dict, set r = r + [s]
            r = {'':r, '.':r, '..':r[:-1]}.get(s, r + [s])
        return '/' + '/'.join(r)

def main():
    path = "/a//b////c/d//././/.."
    obj = Solution()
    result = obj.simplifyPath(path)
    assert result == "/a/b/c", ["hint: result is wrong"]
    print("return result is :",result)
    
if __name__ =='__main__':
    main()   