# leetcode time     cost : 236 ms
# leetcode memory   cost : 13.7 MB
# Time  Complexity: O(N)
# Space Complexity: O(1)
# solution 3 , DP
# https://leetcode-cn.com/problems/knight-dialer/solution/4zhuang-tai-dong-tai-gui-hua-pythonjie-kong-jian-f/
class Solution:
    def knightDialer(self, N: int) -> int:
        if N==1: return 10
        # 5无法跳转，把剩余可跳转状态分为4类，A:{1,3,7,9},B:{2,8},C:{4,6},D:{0}
        # nums[i]分别为状态A,B,C,D
        # 处于状态A中的数字(1,3,7,9)通过一次跳跃要么变成状态B(2,8)，要么变成状态C(4,6)
        # 处于状态B中的数字(2,8)通过一次跳跃有两种方式变成状态A(1,3,7,9)
        # 处于状态C中的数字(4,6)通过一次跳跃有两种方式变成状态A(1,3,7,9)，还有一种方式变成状态D(0)
#       # 处于状态D中的数字(0)通过一次跳跃有两种方式变成状态C(4,6)
        nums=[1,1,1,1]
        max_mod = 10**9 + 7
        for _ in range(N-1):
            # 基于 当前的nums[i] 计算 新的nums[i] 
            nums=[nums[1]+nums[2], 2*nums[0], 2*nums[0]+nums[3], 2*nums[2]]
        #状态A有4个数字，B有2个数字，C有2个数字，D有1个数字
        return (4*nums[0]+2*nums[1]+2*nums[2]+nums[3])%max_mod

def main():
    N = 4551      #expect is 318799568
    obj = Solution()
    res = obj.knightDialer(N)
    print("return value is ",res);
    
if __name__ =='__main__':
    main()    