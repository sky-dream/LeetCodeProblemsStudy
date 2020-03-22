# -*- coding: utf-8 -*-  
# leetcode time     cost : 1696 ms
# leetcode memory   cost : 17.2 MB
# Time  Complexity: O(T∗logT)
# Space Complexity: O(T)
# solution 3, Dijkstra to solve shortest path,
import heapq
class Solution(object):
    def racecar(self, target):
        # 连续加速超过target的最小步数
        K = target.bit_length() + 1
        # 达到2**K 之后必须掉头才可以获取最小步数
        barrier = 1 << K
        direction = 1
        # step already used and the left deviation to target
        pq = [(0, target)]
        # 总的行驶区间为[-barrier,barrier],dist[t] 区间内不同点 t 走到 target 的最小步数
        dist = [float('inf')] * (2 * barrier + 1)
        dist[target] = 0
        while pq:
            # always pop out the min step point from the last BFS layer
            steps, targ = heapq.heappop(pq)
            # pruning, if no point can jump to this point targ,dist[targ]=float('inf'), no need check this point
            if dist[targ] > steps: continue
            # note,need start from 0, car can use 2 R to reset speed back to 1
            for k in range(K+1):
                walk = (1 << k) - 1
                # due to direction change, both walk and targ need to be changed
                walk *= direction
                # add 'R' step when change direction, reverse the recieved target with "-" due to the direction change
                steps2, targ2 = steps + k + 1, walk - targ
                if walk == targ:
                    steps2 -= 1 # No "R" command needed if steps2 already reach the target
                
                # if targ2 in the range and the step from 0 to targ2 is smaller than before,update the min step
                if abs(targ2) <= barrier and (steps2) < dist[targ2]:
                    heapq.heappush(pq, (steps2, targ2))
                    # targ2<0, dist range is the right half,count from right.
                    dist[targ2] = steps2
        return dist[0]


def main():
    target = 16      #expect is 7  
    obj = Solution()
    res = obj.racecar(target)
    print("return value is ",res);
    
if __name__ =='__main__':
    main() 