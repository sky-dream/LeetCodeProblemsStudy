#-*- coding: utf-8 -*-  
# leetcode time     cost : 368 ms
# leetcode memory   cost : 14.4 MB
# Time  Complexity: O(N)
# Space Complexity: O(N)
# solution 3, BFS
class Solution:
    def numSquares(self, n: int) -> int:
        queue = []
        visited =set()
        count = 0
        queue.append(n)
        while (queue):
            size = len(queue)
            count+=1 # 开始生成下一层
            for i in range(size):
                cur = queue.pop(0)
                #依次减 1, 4, 9... 生成下一层的节点
                j = 1
                while (j*j <= cur):
                    # 逐个尝试间隔 平方数 的前一个点的值
                    prev = cur - j*j
                    if (prev == 0):
                        return count
                    if (prev not in visited):
                        queue.append(prev)
                        visited.add(prev)
                    j+=1
        return -1