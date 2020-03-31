# leetcode time     cost : 84 ms
# leetcode memory   cost : 14.1 MB 
# solution 1, stack
# max(depth(A), depth(B))最小，即二者尽可能接近即可，最好按序交替平分左右括号
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> [int]:
        ans = []
        d = 0
        for c in seq:
            if c == '(':
                d += 1
                ans.append(d % 2)
            if c == ')':
                ans.append(d % 2)
                d -= 1
        return ans
    
def main():
    seq = "(()())"        # expect is [1,0,0,0,0,1]
    obj = Solution()
    result = obj.maxDepthAfterSplit(seq)
    print("return result is :",result)
    
if __name__ =='__main__':
    main() 