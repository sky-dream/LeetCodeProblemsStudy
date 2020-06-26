# -*- coding: utf-8 -*-  
# Time  Complexity: O(N)
# Space Complexity: O(N)
# solution 1, stack
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        folder = ""
        n = len(path)
        res = ""
        for i in range(n):
            if path[i]!="/":
                folder += path[i]
            if path[i]=="/" or i==(n-1):
                if folder==".." and len(stack)>0:
                    stack.pop(-1)                   
                # "." and ".." no need add to stack,but "...","...." need
                elif (folder and folder!=".." and folder!="."): 
                    stack.append(folder)
                folder = ""
        #print(stack)  
        if not stack:
            return "/"      
        for i in range(len(stack)):
            res += "/"
            res += stack[i]
        return res

def main():
    path = "/a//b////c/d//././/.."
    obj = Solution()
    result = obj.simplifyPath(path)
    assert result == "/a/b/c", ["hint: result is wrong"]
    print("return result is :",result)
    
if __name__ =='__main__':
    main()   