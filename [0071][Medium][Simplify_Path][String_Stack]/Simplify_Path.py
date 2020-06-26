# -*- coding: utf-8 -*-  
# Time  Complexity: O(N)
# Space Complexity: O(N)
# solution 1, stack
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")

        for item in path:
            if item == "..":
                if stack : stack.pop()
            elif item and item != ".":
                stack.append(item)
        return "/" + "/".join(stack)

def main():
    path = "/a//b////c/d//././/.."
    obj = Solution()
    result = obj.simplifyPath(path)
    assert result == "/a/b/c", ["hint: result is wrong"]
    print("return result is :",result)
    
if __name__ =='__main__':
    main()   