# leetcode time     cost : 724 ms
# leetcode memory   cost : 13.6 MB 
# Time  Complexity: O((N/2)**2)
# Space Complexity: O(1)
# solution 1, sliding window, 2 pointers,
class Solution:
    def findContinuousSequence(self, target: int) -> [[int]]:
        # 初始化窗口指针和输出列表
        i, j, res = 1,2, []

        # 滑动窗口的右边界不能超过target的中值
        while j <= target//2 + 1:
            # 计算当前窗口内数字之和
            cur_sum = sum(list(range(i,j+1)))
            # 若和小于目标，右指针向右移动，扩大窗口
            if cur_sum < target:
                j += 1
            # 若和大于目标，左指针向右移动，减小窗口
            elif cur_sum > target:
                i += 1
            # 相等就把指针形成的窗口添加进输出列表中
            # 别忘了，这里还要继续扩大寻找下一个可能的窗口哦
            else:
                res.append(list(range(i,j+1)))
                # 这里用j+=1，i+=1，i+=2都可以的
                j += 1
        
        return res

def main():
    target = 9          #expect is [[2, 3, 4], [4, 5]]
    Solution_obj = Solution()
    result = Solution_obj.findContinuousSequence(target)
    print("result value is ",result)
    
if __name__ =='__main__':
    main()  