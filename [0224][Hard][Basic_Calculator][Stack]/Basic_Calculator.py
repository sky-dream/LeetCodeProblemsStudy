# solution 2, stack and not reversed string
# Time  Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)
        sign = 1
        temp_int = 0
        res = 0
        num = {'0','1','2','3','4','5','6','7','8','9'}
        i=0
        stack = []
        while i<n:
            if s[i] in num:
                temp_int =  int(s[i]) + temp_int*10
                #print('temp_int:',temp_int)
            elif s[i]=='+':
                res += sign*temp_int
                temp_int = 0
                sign = 1
            elif s[i]=='-':
                res += sign*temp_int
                temp_int = 0
                sign = -1
            
            elif s[i] == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif s[i]==')':
                res += sign*temp_int
                sign = stack.pop()
                prev_res = stack.pop()
                res = res*sign + prev_res
                temp_int =  0
            i+=1 
            #print('i:',i,'res:',res)   
        res = res + sign*temp_int
        return res

def main():
    s = "(1+(4+5+2)-3)+(6+8)"       #expect is 23
    obj = Solution()
    result = obj.calculate(s)
    assert result == 23, ["hint: result is wrong"]
    print("return result is :",result)
    
if __name__ =='__main__':
    main() 