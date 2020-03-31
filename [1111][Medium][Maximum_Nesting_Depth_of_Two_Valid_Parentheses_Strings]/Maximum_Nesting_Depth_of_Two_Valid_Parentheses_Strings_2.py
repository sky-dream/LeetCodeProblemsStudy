# leetcode time     cost : 64 ms
# leetcode memory   cost : 14 MB 
# solution 2, i mod 2 
# max(depth(A), depth(B))最小，即二者尽可能接近即可，最好按序交替平分左右括号
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> [int]:
        ans = list()
        for i, ch in enumerate(seq):
            if ch == '(':
                ans.append(i % 2)
            else:
                ans.append(1 - i % 2)
            # 上面的代码也可以简写成
            # ans.append((i & 1) ^ (ch == '('))
            # C++ 和 Javascript 代码中直接给出了简写的方法
        return ans

def main():
    seq = "(()())"        # expect is [1,0,0,0,0,1]
    obj = Solution()
    result = obj.maxDepthAfterSplit(seq)
    print("return result is :",result)
    
if __name__ =='__main__':
    main() 