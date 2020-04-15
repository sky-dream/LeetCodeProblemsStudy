# leetcode time     cost : 56 ms
# leetcode memory   cost : 17.9 MB 
# Time  Complexity: O(N*logN)
# Space Complexity: O(N)
# solution 3, heap
from heapq import heappush, heappop

class Solution:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        # 每个building的左边界作为起点事件插入list中
        # 每个building的右边界作为结束事件插入list中
        # list按照左边界从小到大, 高度从大到小, 右边界从小到大排序
        events = [(L,-H,R) for L, R, H in buildings]
        events += list({(R, 0, 0) for _, R, _ in buildings})
        events.sort()
        
        # result保存结果
        result = [(0,0)]
        # alive保存仍会影响后续天际线的buildings
        alive = [(0,float("inf"))]
        for pos, negH, R in events:
            while alive[0][1] <= pos:
                # 将已不会影响后续天际线处理的building弹出heap
                heappop(alive)
            if negH:
                # 如果是新加入的building则将building的高度和右边界入堆
                heappush(alive, (negH, R))
            if result[-1][1] != -alive[0][0]:
                result += [[pos, -alive[0][0]]]
        return result[1:]