# leetcode time     cost : 32 ms
# leetcode memory   cost : 13.6 MB 
# Time  Complexity: O(N)
# Space Complexity: O(1)
# solution 3, 间隔法,求根法的进一步优化,
# https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/solution/xiang-jie-hua-dong-chuang-kou-fa-qiu-gen-fa-jian-g/
class Solution:
    def findContinuousSequence(self, target: int) -> [[int]]:
        # 假设起始数字与结尾数字间隔为i,我们的间隔从1开始
        i, res = 1, []
        
        # 根据上面的条件1，限定i的大小，即间隔的范围
        while i*(i+1)/2 < target:
            # 根据条件2，如果x不为整数则扩大间隔
            if not (target - i*(i+1)/2) % (i+1):
                # 如果两个条件都满足，代入公式求出x即可，整除//会把数改成float形式，用int()改回来
                x = int((target - i*(i+1)/2) // (i+1))
                # 反推出y，将列表填入输出列表即可
                res.append(list(range(x,x+i+1)))
            # 当前间隔判断完毕，检查下一个间隔
            i += 1

        # 由于间隔是从小到大，意味着[x,y]列表是从大到小的顺序放入输出列表res的，所以反转之
        return res[::-1]

def main():
    target = 9          #expect is [[2, 3, 4], [4, 5]]
    Solution_obj = Solution()
    result = Solution_obj.findContinuousSequence(target)
    print("result value is ",result)
    
if __name__ =='__main__':
    main()  