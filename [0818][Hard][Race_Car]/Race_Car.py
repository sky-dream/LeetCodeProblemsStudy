# -*- coding: utf-8 -*-  
# leetcode time     cost : 2948 ms
# leetcode memory   cost : 21.9 MB
# Time  Complexity: O(2∗*N)
# Space Complexity: O(N)
# solution 1, BFS,
class Solution:
    def racecar(self, target: int) -> int:
        #dp[i][0] is the position at i step,dp[i][1] is the speed at i step,
        queue = []
        visited = set()
        # init the state,position=0,speed=1,
        queue.append((0,1))
        visited.add((0,1))
        # exclude the R as the first action for pruning,去除第一次动作就倒车的状态
        visited.add((0,-1)) 
        step = 0
        while queue:
            q_size = len(queue)
            while (q_size):
                position,speed = queue.pop(0)
                # update status for action A
                position_A = position+speed
                speed_A = 2*speed
                if position_A==target: return (step+1)
                # pruning,剪枝，提速,剔除位置或速度超过2倍target的情况
                if (abs(position_A)<2*target and abs(speed_A)<2*target):
                    queue.append((position_A,speed_A))
                # update status for action R
                position_R = position
                speed_R = -1 if speed>0 else 1
                # pruning,剪枝，提速，剔除位置和速度已经访问过的状态
                if ((position_R,speed_R) not in visited):
                    queue.append((position_R,speed_R))
                    visited.add((position_R,speed_R))
                q_size-=1
            step+=1
        return -1

def main():
    target = 6      #expect is 5  
    obj = Solution()
    res = obj.racecar(target)
    print("return value is ",res);
    
if __name__ =='__main__':
    main() 