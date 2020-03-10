# leetcode time     cost : 260 ms
# leetcode memory   cost : 13.6 MB 
# Time  Complexity: O(N)
# Space Complexity: O(1)
# solution 2, 求根法,结果是一个等差数列,基于等差数列求和
# https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/solution/xiang-jie-hua-dong-chuang-kou-fa-qiu-gen-fa-jian-g/
class Solution:
    def findContinuousSequence(self, target: int):
        # 创建输出列表
        res = []

        # y不能超过target的中值,即y<=target//2 + 1,range函数左开右闭,所以这里是+2
        for y in range(1,target//2 + 2):
            # 应用我们的求根公式
            x = (1/4 + y**2 + y - 2 * target) ** (1/2) + 0.5
            # 我们要确保x不能是复数，且x必须是整数
            if type(x) != complex and x - int(x) == 0:
                res.append(list(range(int(x),y+1)))
        
        return res

def main():
    target = 9          #expect is [[2, 3, 4], [4, 5]]
    Solution_obj = Solution()
    result = Solution_obj.findContinuousSequence(target)
    print("result value is ",result)
    
if __name__ =='__main__':
    main()  