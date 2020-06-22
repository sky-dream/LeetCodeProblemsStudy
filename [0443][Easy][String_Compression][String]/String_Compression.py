# solution 1,counting char with stack
# leetcode time     cost : 80 ms
# leetcode memory   cost : 13.8 MB 
# Time  Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def compress(self, chars) -> int:
        n = len(chars)
        chars.append(chars[0])
        stack = list()
        for i in range(n):
            # add new char
            if i>0 and chars[i]!=chars[i-1]:                   
                chars.append(chars[i])
                stack = []
            # save the same char to stack 
            if stack==[] or chars[i]==stack[-1]:
                stack.append(chars[i])            
            # calc char counter
            if len(stack) >1 and (i==n-1 or chars[i]!=chars[i+1]):
                chars+=list(str(len(stack)))
            #print(chars,",i: ",i,",stack: ",stack)
        for i in range(n):
            chars.pop(0)
        return len(chars)
    
def main():
    chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b","c","c","c"]
    obj = Solution()
    res = obj.compress(chars)
    print("return value is "+str(res));
    
if __name__ =='__main__':
    main()     