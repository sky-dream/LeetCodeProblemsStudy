# leetcode time     cost : 52 ms
# leetcode memory   cost : 13.8 MB 
# Time  Complexity: O(N*sum)
# Space Complexity: O(N)
# solution 1, DP, refer to 494, add +,- for num in nums to get a target
# 可以变成 选出一些数字，使得它们最逼近整个数组和除以二的值，而最后的结果，就是abs（这个数-总和除以二）*2
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        target = sum(stones)/2.0
        candidates = {0}
        for x in stones:
            addition = set()
            # 把所有可以选出来逼近target的 数据集的 和 放入 求和后的集合 addition
            for y in candidates:
                s = x+y
                # 检查是否已发现最优解，若存在，则提前结束循环
                if s==target:
                    return 0
                elif x+y< target:
                    addition.add(s)
            candidates = candidates.union(addition)
        return int(2*(target-max(candidates)))